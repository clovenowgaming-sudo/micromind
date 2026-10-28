# MicroMind

Model bahasa untuk coding dan pengembangan aplikasi, format GGUF (Q8_0, ±1.6 GB) untuk llama.cpp.

## Asal model
- Berbasis **Qwen2.5-Coder-1.5B-Instruct** oleh Qwen Team / Alibaba Cloud (lisensi Apache-2.0), yang sudah dilatih pada kode dan teks multibahasa (termasuk Inggris dan Indonesia) dalam skala sangat besar.
- Perubahan: dikonversi ke GGUF Q8_0, nama diganti MicroMind, dan system prompt bawaan diganti agar berperan sebagai asisten coding.

## Cara pakai
```
llama-cli -m MicroMind.gguf -c 4096 -t 4
llama-server -m MicroMind.gguf --host 127.0.0.1 --port 8080 -c 4096 -t 4 --api-key KUNCI
```
