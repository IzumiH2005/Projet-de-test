import subprocess, sys, os, glob, shutil, tarfile, time, wave
def sh(c):
    print(">>", c, flush=True); r = subprocess.run(c, shell=True)
    if r.returncode: print("EXIT", r.returncode, flush=True)
    return r.returncode
sh("nvidia-smi")
sh("pip install -q 'piper-tts[train]==1.8.0' cython onnxscript")
import re, importlib.util
mp = os.path.join(os.path.dirname(importlib.util.find_spec("piper").origin), "train/__main__.py")
src = open(mp).read()
src2 = re.sub(r"\n\s*ModelCheckpoint\(\s*monitor=\"val_mos\".*?\),\n", "\n", src, flags=re.S)
print("patch val_mos:", src != src2, flush=True); open(mp, "w").write(src2)
PYX = 'cimport cython\nfrom cython.parallel import prange\n\n\n@cython.boundscheck(False)\n@cython.wraparound(False)\ncdef void maximum_path_each(int[:,::1] path, float[:,::1] value, int t_y, int t_x, float max_neg_val=-1e9) nogil:\n  cdef int x\n  cdef int y\n  cdef float v_prev\n  cdef float v_cur\n  cdef float tmp\n  cdef int index = t_x - 1\n\n  for y in range(t_y):\n    for x in range(max(0, t_x + y - t_y), min(t_x, y + 1)):\n      if x == y:\n        v_cur = max_neg_val\n      else:\n        v_cur = value[y-1, x]\n      if x == 0:\n        if y == 0:\n          v_prev = 0.\n        else:\n          v_prev = max_neg_val\n      else:\n        v_prev = value[y-1, x-1]\n      value[y, x] += max(v_prev, v_cur)\n\n  for y in range(t_y - 1, -1, -1):\n    path[y, index] = 1\n    # NOTE (2026-09-28): added `y > 0` guard. With wraparound(False),\n    # value[y-1, ...] at y == 0 reads out of bounds and segfaults\n    # (seen live: SIGSEGV in maximum_path_c on a batch where the\n    # backtrack had not reached index 0 by y == 0). The wraparound read\n    # was meaningless anyway since the loop ends at y == 0.\n    if y > 0 and index != 0 and (index == y or value[y-1, index] < value[y-1, index-1]):\n      index = index - 1\n\n\n@cython.boundscheck(False)\n@cython.wraparound(False)\ncpdef void maximum_path_c(int[:,:,::1] paths, float[:,:,::1] values, int[::1] t_ys, int[::1] t_xs) nogil:\n  cdef int b = paths.shape[0]\n  cdef int i\n  for i in prange(b, nogil=True):\n    maximum_path_each(paths[i], values[i], t_ys[i], t_xs[i])\n'
import piper; pkg = os.path.dirname(piper.__file__)
ma = os.path.join(pkg, "train/vits/monotonic_align")
open(os.path.join(ma,"core.pyx"),"w").write(PYX)
sh(f"cd {ma} && mkdir -p monotonic_align && cythonize -i core.pyx && mv core*.so monotonic_align/")
W = "/kaggle/temp/data"; os.makedirs(W, exist_ok=True)
tars = glob.glob("/kaggle/input/**/piper_narrateur.tar", recursive=True)
print("tars", tars, flush=True)
if tars:
    sh(f"tar xf {tars[0]} -C {W}")
else:  # dataset déjà décompressé
    src = os.path.dirname(glob.glob("/kaggle/input/**/metadata.csv", recursive=True)[0])
    shutil.copytree(src, W, dirs_exist_ok=True)
import collections
g = collections.defaultdict(list)
for f in glob.glob(f"{W}/audio/r*_*.wav"): g[os.path.basename(f).rsplit("_",1)[0]].append(f)
for k, fs in g.items():
    good = [f for f in fs if os.path.getsize(f) > 1000]
    for f in fs:
        if os.path.getsize(f) <= 1000:
            os.remove(f); shutil.copy(good[0], f)
bad = [f for f in glob.glob(f"{W}/audio/*.wav") if os.path.getsize(f) <= 1000]
print("fichiers vides restants:", len(bad), flush=True)
print(os.listdir(W), flush=True)
OUT = "/kaggle/working"
RUN = "/kaggle/temp/run"
t0 = time.time()
sh(f"cd {W} && PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True python -m piper.train fit --data.voice_name narrateur --data.csv_path metadata.csv "
   f"--data.audio_dir audio --model.sample_rate 22050 --data.espeak_voice fr --data.cache_dir cache "
   f"--data.config_path config.json --data.batch_size 16 --data.num_workers 4 "
   f"--trainer.accelerator gpu --trainer.devices 1 --trainer.max_time 00:04:30:00 "
   f"--trainer.max_epochs 100000 --trainer.log_every_n_steps 20 --trainer.check_val_every_n_epoch 5 "
   f"--trainer.default_root_dir {RUN} --trainer.enable_progress_bar false "
   f"--model.warmstart_ckpt siwis_sd.ckpt --model.mos_metric none 2>&1 | tail -c 200000")
print("train minutes", (time.time() - t0) / 60, flush=True)
ck = sorted(glob.glob(f"{RUN}/**/*.ckpt", recursive=True), key=os.path.getmtime)
print("ckpts", ck, flush=True)
last = [c for c in ck if os.path.basename(c).startswith("last")] or ck
last = last[-1]
shutil.copy(last, f"{OUT}/last.ckpt")
best = [c for c in ck if "val_mel=" in c]
if best:
    b = min(best, key=lambda c: float(c.split("val_mel=")[1][:-5])); print("best", b)
sh(f"python -m piper.train.export_onnx --checkpoint {OUT}/last.ckpt --output-file {OUT}/narrateur.onnx")
shutil.copy(f"{W}/config.json", f"{OUT}/narrateur.onnx.json")
for d in glob.glob(f"{RUN}/**/version_*", recursive=True):
    for m in glob.glob(f"{d}/metrics*.csv") + glob.glob(f"{d}/events*"):
        shutil.copy(m, OUT)
try:
    from piper import PiperVoice
    v = PiperVoice.load(f"{OUT}/narrateur.onnx")
    T = ["Il était une fois, dans un royaume oublié, un vieux narrateur qui racontait des histoires.",
         "La nuit tombait doucement sur la ville, et personne ne savait encore ce qui allait arriver.",
         "Bonjour ! Aujourd'hui, nous allons découvrir ensemble un endroit vraiment extraordinaire."]
    for i, t in enumerate(T):
        with wave.open(f"{OUT}/test_{i}.wav", "wb") as wf:
            v.synthesize_wav(t, wf)
except Exception as e:
    print("synth err", repr(e))
sh(f"ls -la {OUT}")
