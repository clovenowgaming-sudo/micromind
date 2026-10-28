import os
from huggingface_hub import snapshot_download

# Model dasar: Qwen2.5-Coder-1.5B-Instruct (Apache-2.0), sudah dilatih pada kode dalam jumlah sangat besar.
BASE = "Qwen/Qwen2.5-Coder-1.5B-Instruct"
OLD = "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."
NEW = ("Kamu adalah MicroMind, asisten AI untuk coding dan pengembangan aplikasi. "
       "Tulis kode lengkap yang bisa langsung dijalankan, jelaskan singkat, "
       "dan jawab dengan bahasa yang dipakai pengguna.")

snapshot_download(BASE, local_dir="base",
                  allow_patterns=["*.json", "*.safetensors", "*.txt", "*.jinja"])

patched = 0
for fn in os.listdir("base"):
    if fn.endswith((".json", ".jinja")):
        p = os.path.join("base", fn)
        s = open(p, encoding="utf-8").read()
        if OLD in s:
            open(p, "w", encoding="utf-8").write(s.replace(OLD, NEW))
            patched += 1
            print("patch system prompt:", fn)
if patched == 0:
    print("PERINGATAN: system prompt bawaan tidak ditemukan, nama model di jawaban tetap bawaan.")
print("Selesai. File:", sorted(os.listdir("base")))
