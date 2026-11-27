# Briefing Proyek Akhir — Deep Learning S1 (Kelas A)

> **Sumber**: Panduan Proyek Akhir Deep Learning S1 — Kelas A (Last modified: 24 November 2026, 2:53 PM)  
> **Periode Proyek**: 24 November – 15 Desember 2026 (3 minggu, 3 tahap pengumpulan)  
> **Prinsip Utama**: Setiap tim mengerjakan **satu paper** dan **satu perbaikan yang berbeda**.

---

## 1. Identitas Tim & Proyek

> Briefing khusus operasional, teknis, dan pembagian kerja paket terpilih tersedia di [BRIEFING_P04_SAM2.md](./BRIEFING_P04_SAM2.md).

| Komponen | Keterangan |
| :--- | :--- |
| **Mata Kuliah / Kelas** | Deep Learning S1 — Kelas A |
| **Kode & Nama Paket** | **P04 · SAM 2** — titik tambahan dari area yang disepakati dua mask |
| **Judul Paper Utama** | *SAM 2: Segment Anything in Images and Videos* (ICLR 2025) |
| **Judul Naskah Proyek** | `[Menyusul saat penyusunan draf Tahap 1]` |
| **Perangkat Utama** | Google Colab (GPU gratis — mode FP32 tanpa `autocast` BF16 jika GPU tidak mendukung BF16) |
| **Tautan Repo / Colab Tim** | `[Isi setelah repo/notebook tim dibuat]` |
| **Target Tim** | Prioritas nilai maksimal mata kuliah (100 poin sesuai rubrik), dengan dokumentasi & eksperimen rapi agar siap dikembangkan menuju publikasi bila hasil menjanjikan. |

### Daftar Anggota Tim (Maksimal 3 Orang)

| No | Nama Lengkap | NIM | Peran / Kontribusi Utama *(Usulan Awal)* |
| :-: | :--- | :--- | :--- |
| 1 | **Raditya Ramadhan Eka Widhianto** | `245150207111054` | Lead Evaluasi, Pipeline Dataset COCO (Val/Test & Titik Awal), & Integrasi Naskah |
| 2 | **Mochammad Fani Al Gibran** | `245150207111008` | Setup Colab SAM 2 Hiera Tiny, Baseline 1-Titik, & Modul Perbaikan Modular (Toggleable) |
| 3 | **Muhammad Sulthon Aulia Wijaya** | `245150207111103` | Kajian Literatur (SAM 2 & BALD-SAM), Analisis Metrik, & Visualisasi Contoh Berhasil/Gagal |

---

## 2. Gambaran Umum & Pembentukan Tim

- **Komposisi Kelas A**: 41 mahasiswa aktif. Susunan yang disarankan adalah **13 tim berisi 3 orang** dan **1 tim berisi 2 orang** (total 14 tim, maksimal 3 anggota per tim).
- **Ketersediaan Paket**: Tersedia **14 paket utama (`P01`–`P14`)** untuk pembagian awal, serta **`P15` (TimesFM)** sebagai paket cadangan.
- **Koordinasi Pemilihan Paket**:
  1. Pada awal minggu pertama, pilih sendiri satu paket yang masih tersedia sesuai minat dan kemampuan perangkat tim.
  2. Sampaikan **kode paket** dan **daftar anggota** kepada **koordinator kelas** untuk dicatat pada satu daftar yang dapat dilihat seluruh kelas.
  3. **Satu kode paket hanya untuk satu tim.** Jika dua tim memilih paket yang sama, koordinasikan dan gunakan paket lain yang masih tersedia untuk salah satu tim.
- **Validasi Awal & Ganti Paket**:
  - Setelah pilihan dicatat, segera jalankan contoh kode dari repositori penulis pada data kecil.
  - Jika ada kendala akses atau perangkat sehingga tim perlu berganti paket, pilih paket lain yang masih tersedia dan segera beri tahu koordinator kelas agar daftar diperbarui.
- **Prinsip Eksperimen Ringkas**:
  - Mulai dari eksperimen kecil; **satu dataset atau lingkungan sudah cukup** untuk tugas inti.
  - Gunakan *checkpoint* pralatih jika tersedia.
  - Jika paket memerlukan pelatihan, jalankan **satu konfigurasi ringkas** dengan pengaturan yang sama untuk metode asli dan metode usulan.
  - **Penting**: Angka percobaan proyek tim harus dilaporkan **terpisah** dari angka asli yang tertulis pada paper.

---

## 3. Jadwal & Tahap Pengumpulan

> [!IMPORTANT]
> **Pengingat Waktu (per 27 November 2026)**: Tenggat **Tahap 1 (Pendahuluan)** adalah **Selasa, 1 Desember 2026 pukul 23.59 WIB** (tersisa sekitar **4 hari**). Pembentukan tim, penetapan paket ke koordinator, dan verifikasi jalan satu contoh kode harus diprioritaskan di awal.

Proyek berlangsung selama tiga minggu (**24 November – 15 Desember 2026**). Tim menulis **satu naskah paper ilmiah** yang dilengkapi dari minggu ke minggu dan mengumpulkan versi terbaru pada setiap tahap.

| Tahap | Tenggat | Yang Dikumpulkan | Poin |
| :--- | :--- | :--- | :-: |
| **1 · Pendahuluan** | **Selasa, 1 Desember 2026, 23.59 WIB** | Draf paper berisi bagian **Pendahuluan**: masalah yang diteliti, mengapa masalah itu penting, keterbatasan metode asli yang ingin ditangani, diakhiri dengan tujuan, hipotesis, dan ringkasan perbaikan yang akan diuji. Cantumkan paper utama pada Daftar Pustaka. | **15** |
| **2 · Metode dan Hasil Awal** | **Selasa, 8 Desember 2026, 23.59 WIB** | Versi baru paper dengan bagian **Metode** dan **Hasil Awal** (lanjutan Pendahuluan): jelaskan metode asli, perbaikan yang diterapkan, data, pembagian data, metrik, dan pengaturan eksperimen. Tampilkan **hasil baseline** dan **satu bukti prototipe berjalan pada data validasi**. Sertakan tautan repositori atau ZIP beserta perintah untuk menjalankan kode. | **30** |
| **3 · Paper Lengkap** | **Selasa, 15 Desember 2026, 23.59 WIB** | **Paper lengkap** dan **kode versi akhir**: susun naskah dengan *Abstrak, Pendahuluan, Metode, Hasil, Pembahasan, Kesimpulan, dan Daftar Pustaka*. Tampilkan tabel hasil data uji untuk **metode asli**, **pembanding sederhana atau varian tanpa komponen utama**, dan **metode usulan**. Bahas kinerja, biaya komputasi, contoh berhasil dan gagal, serta keterbatasan. Tulis kesimpulan yang menjawab hipotesis dan cantumkan kontribusi setiap anggota. | **55** |

### Ketentuan Format Naskah & Target Mingguan
- **Identitas wajib pada naskah**: Judul paper, kode paket (`P01`–`P15`), nama lengkap, dan NIM seluruh anggota.
- **Template**: Struktur paper ilmiah dengan template bebas.
- **Target sebelum masuk minggu ketiga**: Metode asli sudah menghasilkan angka pembanding dan prototipe perbaikan sudah dapat diuji. Jika masih ada kendala, gunakan hasil Tahap 2 untuk memperkecil cakupan percobaan **dengan persetujuan dosen**. Waktu pada minggu terakhir dipakai untuk membandingkan metode dan menganalisis hasil.

---

## 4. Ketentuan Eksperimen & Standar Ilmiah

Paper pada seluruh paket dipilih berdasarkan publikasi resmi pada jalur utama konferensi dalam rentang **24 November 2023 – 24 November 2026**, dengan contoh kode yang mengarah ke dokumentasi resmi penulis.

1. **Jalankan Pembanding Asli (*Baseline*)**
   - Mulai dari contoh kode yang ditautkan pada paket.
   - Catat: **commit hash**, **versi dependensi/pustaka**, **nama/file bobot (checkpoint)**, **pembagian data (split)**, dan **perangkat (CPU/GPU)** pada bagian Metode.
   - Tunjukkan **satu keluaran yang dapat diperiksa** pada satu contoh sebelum melanjutkan ke subset lebih besar.
2. **Implementasikan Perbaikan Secara Modular**
   - Tempatkan perubahan pada fungsi atau modul yang **bisa diaktifkan dan dimatikan** (*toggleable* untuk ablasi/perbandingan).
   - Gunakan **data validasi** untuk menetapkan ambang (*threshold*) atau hyperparameter.
   - **Simpan data uji** secara terpisah khusus untuk perbandingan akhir (jangan menyetel ambang pada data uji).
3. **Uji Mekanisme Secara Adil**
   - Bandingkan minimal tiga kondisi:
     1. **Pembanding asli** (*baseline* paper),
     2. **Pembanding sederhana atau varian tanpa komponen utama** (ablasi),
     3. **Metode usulan** (perbaikan pada paket).
   - Gunakan sampel, masukan, *checkpoint*, dan batas komputasi yang sebanding.
   - Untuk percobaan acak, gunakan **seed berpasangan** (*paired seeds*). Laporkan selisih per sampel atau per episode bila memungkinkan.
4. **Jelaskan Batas Hasil**
   - Wajib memuat: **satu hipotesis**, **hasil utama**, **satu contoh berhasil**, dan **satu contoh gagal**, serta **pengaruh biaya komputasi**.
   - Hasil yang belum menunjukkan peningkatan angka tetap dinilai baik apabila kualitas pengujian, kontrol eksperimen, dan analisisnya kuat.

---

## 5. Rubrik Penilaian (Total 100 Poin)

| Aspek | Tahap | Poin | Bukti yang Dinilai |
| :--- | :-: | :-: | :--- |
| **Pendahuluan dan hipotesis** | 1 | **15** | Masalah dan konteks paper dijelaskan secara tepat. Keterbatasan, tujuan, dan hipotesis terhubung dengan perbaikan pada paket. |
| **Pembanding asli** | 2 | **20** | Kode berjalan, metrik baseline dicatat, dan pengaturan eksperimen dapat dilacak. |
| **Prototipe perbaikan** | 2 | **10** | Perubahan utama sudah diterapkan dan menghasilkan keluaran awal pada validasi. |
| **Implementasi akhir** | 3 | **15** | Implementasi sesuai paket, dapat dijalankan, dan dapat dibandingkan dengan metode asli. |
| **Bukti dan analisis** | 3 | **25** | Data uji terpisah, pembanding adil, uji komponen, serta analisis biaya dan kegagalan. |
| **Dokumentasi dan presentasi** | 3 | **15** | Langkah reproduksi jelas dan setiap anggota memahami kontribusinya. |

**Catatan Presentasi & Kode Akhir**:
- Sertakan **perintah yang jelas** untuk menjalankan pembanding dan metode usulan pada kode akhir.
- Saat presentasi (jadwal mengikuti dosen), **setiap anggota** wajib menjelaskan kontribusinya dan menjawab pertanyaan tentang keputusan eksperimen.

---

## 6. Pengelompokan Paket Berdasarkan Perangkat

> Referensi kuota Colab: [Batas sumber daya Google Colab](https://research.google.com/colaboratory/faq.html#resource-limits). Jenis GPU, kuota, dan durasi sesi Colab gratis dapat berubah sewaktu-waktu.

| Kategori Perangkat | Paket yang Cocok | Catatan Teknis |
| :--- | :--- | :--- |
| **CPU untuk eksperimen kecil** *(laptop tanpa GPU / Colab CPU)* | **P01** MobileCLIP, **P03** Depth Anything V2, **P08** TabICL, **P09** YOLOv10, **P11** ModernBERT, **P14** XFeat, **P15** TimesFM *(cadangan)* | Bisa dimulai langsung di CPU lokal atau Colab CPU pada subset kecil. P01/P03/P09/P11 bisa dipercepat dengan GPU Colab jika tersedia. |
| **GPU Colab gratis disarankan** | **Pelatihan**: P02 iTransformer, P07 LGA<br>**Contoh model (inferensi)**: P04 SAM 2, P05 SANA, P10 HVI/CIDNet<br>**Pengujian dua arah**: P12 SEA-RAFT, P13 CoTracker3 | P02 & P07 dapat dicek di CPU untuk uji singkat, namun butuh GPU untuk 1 pelatihan penuh. P10 memanggil `.cuda()` langsung. P12 & P13 bisa dicoba sangat kecil di CPU, lalu pindah ke GPU Colab. |
| **GPU CUDA dan simulator** | **P06** TD-MPC2 | Memerlukan pemasangan **DMControl** dan **MuJoCo**. Instalasi paling rumit; **pilih hanya setelah 1 episode uji berhasil** di perangkat yang akan dipakai. |

---

## 7. Matriks Perbandingan Cepat 15 Paket (P01–P15)

| Kode | Model & Venue | Domain | Tipe | Perangkat Utama | Dataset / Benchmark | Inti Perbaikan yang Diuji |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| **P01** | MobileCLIP *(CVPR 2024)* | Vision-Language | Inferensi | CPU / Colab CPU | EuroSAT (bersih & blur) | Pilih 25% citra untuk pemeriksaan ulang *center crop* memakai gabungan peringkat margin probabilitas & varians Laplacian |
| **P02** | iTransformer *(ICLR 2024)* | Time Series | 1 Pelatihan | GPU Colab gratis | `ETTm1.csv` | Gabungkan prediksi iTransformer + pola musiman harian dengan bobot adaptif berbasis galat median 24 prediksi terakhir |
| **P03** | Depth Anything V2 *(NeurIPS 2024)* | Monocular Depth | Inferensi | CPU / Colab CPU | NYU Depth V2 | Penggabungan peta jarak 2 skala (`392` & `518`) dengan bobot Sobel (0,8 skala besar + 0,2 skala kecil di tepi tajam persentil >80) |
| **P04** | SAM 2 *(ICLR 2025)* | Segmentation | Inferensi | GPU Colab gratis | COCO (subset) | Jika IoU 2 mask teratas < 0,6, ambil titik kedua dari irisan kedua mask setelah erosi 3×3 (titik terjauh dari titik awal) |
| **P05** | SANA *(ICLR 2025)* | Text-to-Image Diffusion | Inferensi | GPU Colab gratis | 24 prompt kustom (dengan pasangan atribut) | Buat gambar awal 8 langkah; skor kecocokan atribut via CLIP; regenerasi 50% terburuk dengan 16 langkah |
| **P06** | TD-MPC2 *(ICLR 2024)* | Model-Based RL | Inferensi + Sim | GPU CUDA + MuJoCo | DMControl (`dog-run`) | Anggaran kandidat perencanaan adaptif (1,25× saat perubahan keadaan > persentil 70 validasi, 0,75× saat stabil) |
| **P07** | Local Geometry Attention *(ICLR 2026)* | Time Series | 1 Pelatihan | GPU Colab gratis | `ETTh1.csv` + lonjakan TSRBench | Filter lonjakan kausal berbasis median & MAD 11 titik sebelumnya (ganti jika selisih > `4,5 × (MAD + ε)`) |
| **P08** | TabICL *(ICML 2025)* | Tabular Classification | Inferensi | CPU / Colab CPU | OpenML 1464 (*Blood Transfusion*) | Pemilihan 128 konteks dengan kuota minimal 8 tetangga terdekat per kelas sebelum sisa diisi tetangga terdekat global |
| **P09** | YOLOv10 *(NeurIPS 2024)* | Object Detection | Inferensi | CPU / Colab CPU | COCO `val2017` (subset, *tiling* 20%) | Penggabungan kotak di sambungan potongan dengan bobot jarak dari tepi potongan: `skor × min(1, max(0.1, d/32))` |
| **P10** | HVI/CIDNet *(CVPR 2025)* | Low-Light Enhancement | Inferensi | GPU Colab gratis | LOLv1 (validasi & uji terpisah) | Di ruang CIELAB, pertahankan L hasil model dan campur 25% warna (a,b) foto redup pada piksel ber-L>10 & pergeseran warna > ambang |
| **P11** | ModernBERT *(ACL 2025)* | Information Retrieval | Cache Embedding | CPU / Colab CPU | SciFact | Weighted RRF antara ModernBERT & BM25 dengan bobot dinamis (BM25 0,7 jika kueri ber-IDF tinggi & overlap top-5 < ambang) |
| **P12** | SEA-RAFT *(ECCV 2024)* | Optical Flow | Inferensi 2-arah | GPU Colab *(uji kecil CPU)* | Sintel | Uji konsistensi maju-balik; perbaiki piksel dengan galat pulang-pergi > ambang memakai median ≥3 tetangga 3×3 yang konsisten |
| **P13** | CoTracker3 *(ICCV 2025)* | Point Tracking | Klip Pendek 2-arah | GPU Colab *(uji kecil CPU)* | TAP-Vid DAVIS | Lacak balik dari bingkai terakhir terlihat; tandai titik tertutup jika jarak maju-balik > ambang pada 2 bingkai berturut-turut |
| **P14** | XFeat *(CVPR 2024)* | Feature Matching | Inferensi | CPU / Colab CPU | HPatches | Dari 2.048 kandidat, pilih hingga 32 titik terbaik per sel pada kisi 4×4 (sisa diisi skor tertinggi) total maksimal 512 titik |
| **P15** | TimesFM *(ICML 2024)* *(Cadangan)* | Time Series | Inferensi | CPU / Colab CPU | Deret > 512 titik | Uji 3 panjang riwayat (128, 256, 512) pada 3 titik historis; pilih riwayat terpendek dengan galat ≤ `1,01 × galat terbaik` |

---

## 8. Rincian Lengkap Tiap Paket (P01–P15)

### P01 · MobileCLIP — Memilih Citra yang Perlu Diperiksa Dua Kali
- **Info**: CVPR 2024 · Ringan · Inferensi
- **Tautan**: [Paper Asli](https://machinelearning.apple.com/research/mobileclip) · [Repo GitHub](https://github.com/apple-aiml-research/ml-mobileclip) · [Contoh Kode (README · V1-only usage example)](https://github.com/apple-aiml-research/ml-mobileclip/blob/main/README.md) · [Skrip Bobot (`get_pretrained_models.sh`)](https://github.com/apple-aiml-research/ml-mobileclip/blob/main/get_pretrained_models.sh) · [Halaman Paket](https://brone.ub.ac.id/mod/page/view.php?id=246059&forceview=1#P01)
- **Gambaran & Masalah**: Pada citra satelit EuroSAT yang buram, detail seperti pepohonan vs lahan pertanian sulit dibedakan. Evaluasi dilakukan pada foto EuroSAT sebelum dan sesudah diberi blur untuk melihat berapa prediksi berubah dari benar menjadi salah, dan apakah ukuran keburaman membantu memilih 25% foto untuk diperiksa ulang lewat potongan tengah (*center crop*).
- **Mulai dari Kode**: Unduh `mobileclip_s0.pt` dari `get_pretrained_models.sh`. Salin potongan Python *V1-only usage example* (`encode_image` & `encode_text`). Pakai bobot dan prompt tetap saat beralih ke EuroSAT.
- **Perangkat**: CPU atau Colab gratis tanpa GPU untuk MobileCLIP-S0 pada subset kecil (gunakan `torch.no_grad()` tanpa `torch.cuda.amp.autocast()` di CPU).
- **Perbaikan yang Dibuat**:
  1. Jalankan MobileCLIP sekali pada tiap gambar; catat selisih probabilitas kelas peringkat 1 dan 2.
  2. Hitung **varians Laplacian** tiap gambar (nilai kecil = lebih buram).
  3. Dalam tiap batch, buat 2 peringkat: selisih probabilitas terkecil dan varians Laplacian terkecil. Jumlahkan kedua nomor peringkat dan pilih **25%** gambar dengan jumlah terkecil.
  4. Untuk gambar terpilih, jalankan ulang model pada *center crop*, rata-ratakan **logit** (sebelum softmax) gambar utuh + potongan tengah, lalu ambil kelas tertinggi.
- **Cara Uji & Pelaporan**: Uji pada EuroSAT bersih dan blur. Bandingkan: (1) gambar utuh saja, (2) pemeriksaan ulang 25% berdasarkan selisih probabilitas terkecil saja, (3) pemeriksaan ulang 25% berdasarkan gabungan dua peringkat. Laporkan **akurasi** dan **rata-rata jumlah pemanggilan model per gambar**.

---

### P02 · iTransformer — Menggabungkan Prediksi Model dan Pola Musiman
- **Info**: ICLR 2024 · GPU Ringan · Satu Pelatihan
- **Tautan**: [Paper Asli](https://proceedings.iclr.cc/paper_files/paper/2024/file/2ea18fdc667e0ef2ad82b2b4d65147ad-Paper-Conference.pdf) · [Repo GitHub](https://github.com/thuml/iTransformer) · [Contoh Kode (`iTransformer_ETTm1.sh`)](https://github.com/thuml/iTransformer/blob/main/scripts/multivariate_forecasting/ETT/iTransformer_ETTm1.sh) · [Halaman Paket](https://brone.ub.ac.id/mod/page/view.php?id=246059&forceview=1#P02)
- **Gambaran & Masalah**: Data sensor kadang mengikuti pola harian yang kuat, sementara di waktu lain kondisi berubah sehingga iTransformer lebih akurat. Bobot tetap tidak menangkap pergantian keunggulan ini sepanjang waktu.
- **Mulai dari Kode**: Letakkan `ETTm1.csv` di `dataset/ETT-small/`. Jalankan blok `python -u run.py` pertama di `iTransformer_ETTm1.sh` (`ETTm1_96_96`, `--pred_len 96`). Simpan prediksi dasar.
- **Perangkat**: GPU Colab gratis disarankan (ubah `CUDA_VISIBLE_DEVICES=2` menjadi `0`). `run.py` mendukung CPU jika CUDA tidak ada (cocok untuk uji pendek).
- **Perbaikan yang Dibuat**:
  1. Siapkan 2 perkiraan 96 langkah ke depan: (a) iTransformer, (b) pola harian (mengulang 96 pengamatan terakhir).
  2. Ambil 24 prediksi terdahulu yang nilai aslinya sudah diketahui saat itu; hitung median selisih absolut masing-masing ($e_{\text{model}}$ dan $e_{\text{musiman}}$).
  3. Hitung bobot $w = \frac{e_{\text{musiman}}}{e_{\text{model}} + e_{\text{musiman}} + \varepsilon}$, lalu gabungkan: $w \cdot \hat{y}_{\text{model}} + (1 - w) \cdot \hat{y}_{\text{musiman}}$. Jika belum ada 24 prediksi ternilai, pakai bobot tetap dari validasi.
- **Cara Uji & Pelaporan**: Uji berurutan dari waktu awal ke akhir pada waktu & target sama untuk: iTransformer saja, pola harian saja, gabungan bobot tetap, dan gabungan bobot adaptif. Laporkan **MAE**, **MSE**, satu contoh kapan pola harian membantu, serta timestamp prediksi & ketersediaan nilai asli untuk verifikasi urutan.

---

### P03 · Depth Anything V2 — Penggabungan Dua Skala di Batas Objek
- **Info**: NeurIPS 2024 · Ringan–Sedang · Inferensi
- **Tautan**: [Paper Asli](https://proceedings.neurips.cc/paper_files/paper/2024/hash/26cfdcd8fe6fd75cc53e92963a656c58-Abstract-Conference.html) · [Repo GitHub](https://github.com/DepthAnything/Depth-Anything-V2) · [Contoh Kode (`metric_depth/run.py`)](https://github.com/DepthAnything/Depth-Anything-V2/blob/main/metric_depth/run.py) · [README `metric_depth`](https://github.com/DepthAnything/Depth-Anything-V2/tree/main/metric_depth) · [Halaman Paket](https://brone.ub.ac.id/mod/page/view.php?id=246059&forceview=1#P03)
- **Gambaran & Masalah**: Pada batas objek (misal pinggiran kursi di depan dinding), model sering keliru memberi perkiraan jarak yang hampir sama. Di sisi lain, garis motif pada dinding bisa tampak tajam padahal jarak kedua sisinya sama.
- **Mulai dari Kode**: Masuk ke `metric_depth/`, unduh bobot Indoor (Hypersim) Small, jalankan `run.py` dengan `--encoder vits`, `--load-from`, `--img-path`, `--save-numpy`. Uji `--input-size 392` dan `518`, lalu terapkan pada NYU Depth V2.
- **Perangkat**: CPU atau Colab CPU cukup untuk Small pada beberapa gambar; GPU Colab gratis jika subset terlalu lambat.
- **Perbaikan yang Dibuat**:
  1. Jalankan checkpoint yang sama pada skala masukan `392` dan `518`; *resize* kedua peta jarak agar sejajar dengan foto asli.
  2. Ubah foto ke luminans, hitung ketajaman tepi menggunakan **Sobel**, dan cari **persentil ke-80**.
  3. Untuk piksel di atas persentil ke-80: `0,8 × jarak(518) + 0,2 × jarak(392)`. Untuk piksel lain: rata-rata `0,5` masing-masing.
- **Cara Uji & Pelaporan**: Pada NYU Depth V2 yang sama, bandingkan satu skala, rata-rata dua skala, dan penggabungan berbobot Sobel. Laporkan **AbsRel** pada seluruh piksel valid dan khusus piksel di sekitar batas perubahan jarak acuan. Periksa juga satu tepi tekstur (motif dinding) yang jaraknya sebenarnya hampir sama.

---

### P04 · SAM 2 — Titik Tambahan dari Area yang Disepakati Dua Mask
- **Info**: ICLR 2025 · GPU · Inferensi
- **Tautan**: [Paper Asli](https://openreview.net/pdf/7c41968163abe4e3700e3e3a15174a9d679fcd52.pdf) · [Repo GitHub](https://github.com/facebookresearch/sam2) · [Contoh Kode (`image_predictor_example.ipynb`)](https://github.com/facebookresearch/sam2/blob/main/notebooks/image_predictor_example.ipynb) · [Colab Resmi](https://colab.research.google.com/github/facebookresearch/sam2/blob/main/notebooks/image_predictor_example.ipynb) · [Checkpoint Hiera Tiny](https://dl.fbaipublicfiles.com/segment_anything_2/072824/sam2_hiera_tiny.pt) · [Pracetak BALD-SAM](https://arxiv.org/abs/2603.10828) · [Halaman Paket](https://brone.ub.ac.id/mod/page/view.php?id=246059&forceview=1#P04)
- **Gambaran & Masalah**: Satu titik awal dalam objek bisa ambigu (misal hanya menandai dudukan kursi alih-alih seluruh kursi), terutama ketika dua kandidat mask dari model berbeda jauh.
- **Mulai dari Kode**: Pasangkan `configs/sam2/sam2_hiera_t.yaml` dengan `sam2_hiera_tiny.pt`. Gunakan titik awal yang sama per objek pada subset COCO menggunakan mask acuan.
- **Perangkat**: Colab gratis dengan GPU. Jika `autocast` BF16 bermasalah di GPU yang didapat, jalankan dalam FP32 dengan menonaktifkan `autocast`.
- **Perbaikan yang Dibuat**:
  1. Beri SAM 2 satu titik awal; simpan dua mask dengan skor tertinggi dan hitung **IoU** keduanya.
  2. Jika `IoU < 0,6`: ambil irisan kedua mask, lakukan **erosi kernel 3 × 3** (jika kosong, simpan prediksi awal).
  3. Pilih piksel di area tersisa yang **paling jauh dari titik awal** sebagai titik positif kedua, lalu jalankan ulang SAM 2 dengan 2 titik. Jika `IoU ≥ 0,6`, pakai prediksi awal.
- **Cara Uji & Pelaporan**: Pada objek COCO dan titik awal yang sama, bandingkan: (1) satu titik, (2) titik kedua dari mask terbaik saja, (3) titik kedua dari area kesepakatan dua mask. Laporkan **IoU terhadap mask acuan** dan **rata-rata jumlah titik per objek**. Tunjukkan kasus saat kedua mask awal sama-sama salah, dan bahas bedanya dengan pendekatan ketidakpastian pada BALD-SAM.

---

### P05 · SANA — Anggaran Difusi Berdasarkan Atribut yang Hilang pada Gambar Awal
- **Info**: ICLR 2025 · GPU · Inferensi
- **Tautan**: [Paper Asli](https://openreview.net/pdf/aec11406cdde431632ff6d7992b303a0686cff7c.pdf) · [Repo GitHub](https://github.com/NVlabs/Sana) · [Contoh Kode (`Sana_600M_512px_diffusers`)](https://huggingface.co/Efficient-Large-Model/Sana_600M_512px_diffusers) · [Pracetak Pembanding](https://arxiv.org/abs/2609.16572) · [Halaman Paket](https://brone.ub.ac.id/mod/page/view.php?id=246059&forceview=1#P05)
- **Gambaran & Masalah**: Pada jumlah langkah difusi yang tetap, prompt mudah langsung sesuai sementara prompt dengan atribut yang terlewat (misal warna salah) tetap gagal.
- **Mulai dari Kode**: Salin blok *How to use SanaPipeline with diffusers* untuk `Efficient-Large-Model/Sana_600M_512px_diffusers` pada ukuran 512 × 512. Siapkan **24 prompt tetap** lengkap dengan pasangan deskripsi benar dan salah untuk setiap ciri sebelum melihat hasil model.
- **Perangkat**: GPU Colab gratis (CUDA + BF16 sesuai halaman checkpoint), satu gambar per pemanggilan. Simpan hasil per seed.
- **Perbaikan yang Dibuat**:
  1. Buat gambar awal per prompt dengan **8 langkah difusi**.
  2. Hitung skor CLIP (bobot tetap) untuk deskripsi benar minus deskripsi salah pada setiap pasangan ciri; ambil **selisih paling kecil** sebagai skor gambar.
  3. Urutkan gambar berdasarkan skor; buat ulang **separuh gambar dengan skor terendah** pada seed yang sama dengan **16 langkah** (rata-rata langkah tetap `8 + 0,5 × 16 = 16`).
- **Cara Uji & Pelaporan**: Ulangi untuk **3 seed yang sama**. Bandingkan dengan: (1) selalu 16 langkah, (2) 50% acak dibuat ulang 16 langkah, (3) pemilihan berdasarkan jumlah ciri di teks prompt. Nilai kemunculan ciri secara *blind* (tanpa melihat nama metode), laporkan **skor pemenuhan ciri**, **waktu total** (termasuk CLIP), dan bahas peran melihat gambar awal vs isi prompt saja.

---

### P06 · TD-MPC2 — Anggaran Perencanaan Adaptif di Simulasi
- **Info**: ICLR 2024 · GPU dan Simulator · Inferensi
- **Tautan**: [Paper Asli](https://openreview.net/pdf/d7962b8e764953c9c4db96aa85307e9e9b689881.pdf) · [Repo GitHub](https://github.com/nicklashansen/tdmpc2) · [Contoh Kode (`tdmpc2/evaluate.py`)](https://github.com/nicklashansen/tdmpc2/blob/main/tdmpc2/evaluate.py) · [Petunjuk Instalasi](https://github.com/nicklashansen/tdmpc2#getting-started) · [Halaman Paket](https://brone.ub.ac.id/mod/page/view.php?id=246059&forceview=1#P06)
- **Gambaran & Masalah**: TD-MPC2 biasanya memeriksa jumlah rencana tindakan tetap per langkah, padahal dinamika keadaan robot berubah cepat pada sebagian langkah dan stabil pada langkah lain.
- **Mulai dari Kode**: Pasang DMControl & MuJoCo sesuai petunjuk penulis, unduh checkpoint `dog-run` (`model_size=5`), jalankan:  
  `python evaluate.py task=dog-run model_size=5 checkpoint=/path/to/checkpoint.pt eval_episodes=1 save_video=false`
- **Perangkat**: **GPU CUDA wajib**. Paket dengan instalasi paling rumit—pastikan 1 episode uji berhasil sebelum memilih paket ini.
- **Perbaikan yang Dibuat**:
  1. Pada episode validasi, ukur perubahan keadaan antar langkah (dinormalisasi terhadap skala tiap fitur dari validasi) dan tetapkan ambang pada **persentil ke-70**.
  2. Saat pengujian, jika perubahan melewati ambang, pakai `~1,25×` jumlah kandidat asli; jika tidak, pakai `~0,75×` (bulatkan ke integer dan minimal sebanyak kandidat *elite*).
- **Cara Uji & Pelaporan**: Pada tugas DMControl yang sama dengan minimal **10 seed episode yang sama**, bandingkan: (1) TD-MPC2 asli, (2) jumlah kandidat tetap yang setara dengan rata-rata kandidat metode usulan, (3) metode adaptif. Laporkan **jumlah kandidat aktual**, **return per episode**, **rata-rata waktu pilih tindakan**, dan **persentil ke-95 waktu pilih tindakan**.

---

### P07 · Local Geometry Attention (LGA) — Koreksi Lonjakan dengan Riwayat Lokal
- **Info**: ICLR 2026 · GPU Ringan · Satu Pelatihan
- **Tautan**: [Paper Asli](https://proceedings.iclr.cc/paper_files/paper/2026/hash/476ab8f369e489c04187ba4f6cfa68-Abstract-Conference.html) · [Repo GitHub](https://github.com/dongbeank/LGA) · [Contoh Kode (`scripts/ETTh1.sh`)](https://raw.githubusercontent.com/dongbeank/LGA/main/scripts/ETTh1.sh) · [Halaman Paket](https://brone.ub.ac.id/mod/page/view.php?id=246059&forceview=1#P07)
- **Gambaran & Masalah**: Satu lonjakan pembacaan sensor dapat mengacaukan ramalan LGA, namun penyaringan berlebih berisiko menghapus perubahan tajam yang memang nyata.
- **Mulai dari Kode**: Simpan `ETTh1.csv` di `dataset/ETT-small/`, jalankan blok `python -u run.py` pertama di `scripts/ETTh1.sh` (`ETTh1_336_96`, horizon 96). Siapkan dua tingkat gangguan lonjakan dari `TSRBench/generate_noise.sh`.
- **Perangkat**: GPU Colab gratis untuk pelatihan; CPU bisa untuk menyiapkan data gangguan dan cek singkat.
- **Perbaikan yang Dibuat**:
  1. Untuk setiap sensor & waktu, ambil **11 pengamatan terdahulu** yang tersedia; hitung **median** dan **MAD** (median selisih absolut terhadap median).
  2. Jika $|x_t - \text{median}| > 4,5 \times (\text{MAD} + \varepsilon)$, ganti $x_t$ dengan median; jika tidak, pertahankan nilai asli (secara kausal).
  3. Masukkan ke model LGA yang sudah dilatih dengan bobot tetap.
- **Cara Uji & Pelaporan**: Pada tiga kondisi (bersih, lonjakan tingkat 1, lonjakan tingkat 2) dengan potongan waktu sama, bandingkan: (1) LGA tanpa penyaringan, (2) filter median ke semua titik, (3) filter median hanya di atas ambang. Laporkan **MAE**, **MSE**, visualisasi potongan deret sebelum & sesudah filter, serta analisis apakah perubahan tajam asli ikut terganti.

---

### P08 · TabICL — Memilih Konteks yang Mewakili Kelas Langka
- **Info**: ICML 2025 · Ringan · Inferensi
- **Tautan**: [Paper Asli](https://proceedings.mlr.press/v267/qu25d.html) · [Repo GitHub](https://github.com/soda-inria/tabicl) · [Contoh Kode (`docs/index.rst` · Quick start)](https://github.com/soda-inria/tabicl/blob/main/docs/index.rst) · [Dataset OpenML 1464](https://www.openml.org/d/1464) · [Studi LoCalPFN](https://proceedings.neurips.cc/paper_files/paper/2024/hash/c40daf14d7a6469e65116507c21faeb7-Abstract-Conference.html) · [Halaman Paket](https://brone.ub.ac.id/mod/page/view.php?id=246059&forceview=1#P08)
- **Gambaran & Masalah**: Memilih contoh konteks (*in-context examples*) hanya berdasarkan kemiripan terdekat dapat menyingkirkan baris dari kelas minoritas.
- **Mulai dari Kode**: Salin contoh `TabICLClassifier` dari `docs/index.rst` dengan `checkpoint_version="tabicl-classifier-v1-20250208.ckpt"`. Gunakan dataset Blood Transfusion Service Center (OpenML 1464) dengan *stratified split* latih, validasi, dan uji.
- **Perangkat**: CPU lokal atau Colab CPU dengan `device="cpu"` (mulai dari beberapa baris uji karena seleksi 128 contoh per baris lebih lama saat evaluasi penuh).
- **Perbaikan yang Dibuat**:
  1. Skalakan fitur numerik memakai statistik data latih; hitung jarak baris uji ke data latih berlabel.
  2. Siapkan maksimal **128 tempat** konteks: masukkan terlebih dahulu **8 baris terdekat dari tiap kelas** (atau sebanyak yang tersedia).
  3. Isi sisa tempat dengan baris terdekat dari kelas mana pun yang belum terpilih (pilihan kuota & ukuran jarak disetel di validasi).
- **Cara Uji & Pelaporan**: Pada baris uji dan jumlah contoh (128) yang sama, bandingkan: (1) acak berstratifikasi, (2) tetangga terdekat tanpa kuota, (3) tetangga terdekat dengan kuota per kelas. Laporkan **balanced accuracy**, **recall kelas minoritas**, dan **waktu inferensi**.

---

### P09 · YOLOv10 — Mengurangi Duplikasi Deteksi di Sambungan Potongan Citra
- **Info**: NeurIPS 2024 · Ringan–Sedang · Inferensi
- **Tautan**: [Paper Asli](https://proceedings.neurips.cc/paper_files/paper/2024/hash/c34ddd05eb089991f06f3c5dc36836e0-Abstract.html) · [Repo GitHub](https://github.com/THU-MIG/yolov10) · [Contoh Kode (README · Prediction)](https://github.com/THU-MIG/yolov10#prediction) · [Rilis Bobot `v1.1`](https://github.com/THU-MIG/yolov10/releases/tag/v1.1) · [Halaman Paket](https://brone.ub.ac.id/mod/page/view.php?id=246059&forceview=1#P09)
- **Gambaran & Masalah**: *Tiling* (memotong gambar) membantu deteksi objek kecil, namun objek di area tumpang tindih sering terdeteksi ganda dan kotak yang dekat tepi potongan cenderung terpotong/meleset.
- **Mulai dari Kode**: Unduh `yolov10n.pt` (rilis v1.1), jalankan `yolo predict model=yolov10n.pt source=contoh.jpg device=cpu`. Lanjutkan pada subset COCO `val2017` dengan potongan bertumpang tindih **20%**.
- **Perangkat**: CPU atau Colab CPU cukup untuk `yolov10n` pada subset kecil; gunakan `device=0` di GPU Colab jika mengevaluasi banyak potongan.
- **Perbaikan yang Dibuat**:
  1. Konversi semua kotak dari potongan (overlap 20%) ke koordinat gambar utuh.
  2. Kelompokkan kotak dengan kelas sama, berasal dari potongan berbeda, dan `IoU ≥ 0,5`.
  3. Ukur jarak $d$ (piksel) dari sisi kotak ke batas potongan terdekat di dalam gambar utuh. Hitung bobot: $\text{skor} \times \min(1, \max(0.1, d/32))$.
  4. Rata-ratakan koordinat secara berbobot dan ambil skor deteksi tertinggi sebagai skor kotak gabungan.
- **Cara Uji & Pelaporan**: Pada foto COCO yang sama, bandingkan: (1) gambar utuh, (2) potongan + penggabungan skor saja, (3) potongan + penggabungan berbobot jarak tepi. Laporkan **AP objek kecil**, **jumlah deteksi ganda di sambungan**, **waktu inferensi**, serta visualisasi satu contoh gambar sebelum & sesudah penggabungan.

---

### P10 · HVI/CIDNet — Mengendalikan Pergeseran Warna pada Hasil Pencerahan
- **Info**: CVPR 2025 · Ringan–Sedang · Inferensi
- **Tautan**: [Paper Asli](https://openaccess.thecvf.com/content/CVPR2025/html/Yan_HVI_A_New_Color_Space_for_Low-light_Image_Enhancement_CVPR_2025_paper.html) · [Repo GitHub](https://github.com/Fediory/HVI-CIDNet) · [Contoh Kode (`eval_hf.py`)](https://github.com/Fediory/HVI-CIDNet/blob/master/eval_hf.py) · [Halaman Paket](https://brone.ub.ac.id/mod/page/view.php?id=246059&forceview=1#P10)
- **Gambaran & Masalah**: Pencerahan foto redup sering menggeser warna objek, sementara bagian yang terlalu gelap pada foto asli memiliki sinyal warna yang tidak andal.
- **Mulai dari Kode**: Jalankan `python eval_hf.py --path Fediory/HVI-CIDNet-LOLv1-wperc --input_img foto_redup.jpg`, cek `output_hf/`. Gunakan dataset **LOLv1** dengan validasi dan uji terpisah.
- **Perangkat**: GPU Colab gratis (karena `eval_hf.py` memanggil `.cuda()` langsung). Evaluasi & koreksi CIELAB bisa dilakukan di CPU setelah keluaran tersimpan.
- **Perbaikan yang Dibuat**:
  1. Konversi foto redup & keluaran CIDNet ke ruang warna **CIELAB** ($L \in [0, 100]$, kanal warna $a, b$).
  2. Tandai piksel jika $L_{\text{redup}} > 10$ dan jarak warna $\Delta_{ab}$ antara foto redup & hasil CIDNet melebihi ambang validasi.
  3. Pada piksel tertandai, campur $(a, b)$ menjadi `0,75 × hasil CIDNet + 0,25 × foto redup`; pertahankan $L$ hasil CIDNet di seluruh gambar.
- **Cara Uji & Pelaporan**: Bandingkan: (1) CIDNet asli, (2) campur 25% warna redup pada semua piksel, (3) campur hanya pada piksel terpilih. Laporkan **$\Delta E$**, **PSNR**, dan **SSIM** terhadap foto normal acuan, serta tampilkan satu contoh saat mengembalikan warna foto redup justru memperburuk hasil.

---

### P11 · ModernBERT — Pembobotan Pencarian Berdasarkan Kesepakatan Hasil
- **Info**: ACL 2025 · Ringan–Sedang · Cache Embedding
- **Tautan**: [Paper Asli](https://aclanthology.org/2025.acl-long.127/) · [Repo GitHub](https://github.com/AnswerDotAI/ModernBERT) · [Contoh Kode (`examples/evaluate_st.py`)](https://github.com/AnswerDotAI/ModernBERT/blob/main/examples/evaluate_st.py) · [Model `ModernBERT-base`](https://huggingface.co/answerdotai/ModernBERT-base) · [Halaman Paket](https://brone.ub.ac.id/mod/page/view.php?id=246059&forceview=1#P11)
- **Gambaran & Masalah**: Pencarian semantik (ModernBERT) dapat melewatkan istilah teknis langka, sedangkan pencarian leksikal (BM25) dapat melewatkan parafrase. Bobot gabungan tetap memperlakukan semua kueri secara sama.
- **Mulai dari Kode**: Buat notebook memakai `AutoTokenizer` & `AutoModel` dari `answerdotai/ModernBERT-base` (rata-rata vektor token non-padding), simpan (*cache*) embedding korpus **SciFact**, dan buat pembanding BM25 pada korpus yang sama.
- **Perangkat**: CPU atau Colab CPU untuk percobaan kecil (simpan embedding sekali agar hemat waktu; GPU Colab dapat membantu saat membuat embedding korpus).
- **Perbaikan yang Dibuat**:
  1. Ambil top-20 dari ModernBERT dan top-20 dari BM25. Hitung irisan dokumen pada top-5 kedua daftar dan cek keberadaan istilah ber-IDF tinggi di kueri.
  2. Jika kesamaan top-5 di bawah ambang validasi **dan** kueri memuat istilah ber-IDF tinggi: bobot BM25 `0,7` & ModernBERT `0,3`; selain itu: BM25 `0,3` & ModernBERT `0,7`.
  3. Gabungkan kedua daftar dengan **weighted Reciprocal Rank Fusion (RRF)**: $\sum \frac{\text{bobot}}{k_{\text{RRF}} + \text{peringkat}}$.
- **Cara Uji & Pelaporan**: Pada koleksi SciFact yang sama, bandingkan ModernBERT saja, BM25 saja, RRF bobot tetap, dan RRF bobot adaptif. Laporkan **nDCG@10** dan **Recall@20**, serta tampilkan hasil khusus kueri beristilah langka.

---

### P12 · SEA-RAFT — Menyaring Aliran Gerak yang Tidak Konsisten
- **Info**: ECCV 2024 · GPU · Inferensi
- **Tautan**: [Paper Asli](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01065.pdf) · [Repo GitHub](https://github.com/princeton-vl/SEA-RAFT) · [Contoh Kode (`custom.py`)](https://github.com/princeton-vl/SEA-RAFT/blob/main/custom.py) · [Halaman Paket](https://brone.ub.ac.id/mod/page/view.php?id=246059&forceview=1#P12)
- **Gambaran & Masalah**: Pada oklusi atau gerak besar, estimasi *optical flow* bisa gagal uji konsistensi pulang-pergi (maju lalu balik tidak kembali ke posisi awal).
- **Mulai dari Kode**: Jalankan `python custom.py --cfg config/eval/spring-M.json --url MemorySlices/Tartan-C-T-TSKH-spring540x960-M --device cpu` dan cek `custom/flow.jpg`. Pilih pasangan konfigurasi & bobot yang sesuai untuk eksperimen **Sintel**.
- **Perangkat**: CPU didukung (`--device cpu`) untuk 1 pasang; gunakan GPU Colab gratis (`--device cuda`) untuk pengujian subset dua arah.
- **Perbaikan yang Dibuat**:
  1. Hitung aliran maju $f$ (bingkai 1→2) dan balik $b$ (bingkai 2→1).
  2. Ukur jarak pulang-pergi $\|f(x) + b(x + f(x))\|$ menggunakan interpolasi bilinear (abaikan piksel yang keluar batas gambar).
  3. Jika jarak melebihi ambang validasi, periksa jendela 3 × 3; jika ada minimal **3 tetangga** yang konsisten ($\le$ ambang), ganti dengan median komponen gerak mereka.
- **Cara Uji & Pelaporan**: Pada pasangan Sintel yang sama, bandingkan gerak maju asli, filter median pada semua piksel, dan filter median selektif (konsistensi). Laporkan **EPE** (seluruh piksel & wilayah gerak besar), **persentase piksel yang berubah**, dan **tambahan waktu** menghitung gerak balik.

---

### P13 · CoTracker3 — Memperbaiki Status Terlihat dengan Uji Balik
- **Info**: ICCV 2025 · GPU · Klip Pendek
- **Tautan**: [Paper Asli](https://openaccess.thecvf.com/content/ICCV2025/papers/Karaev_CoTracker3_Simpler_and_Better_Point_Tracking_by_Pseudo-Labelling_Real_Videos_ICCV_2025_paper.pdf) · [Repo GitHub](https://github.com/facebookresearch/co-tracker) · [Contoh Kode (`demo.py`)](https://github.com/facebookresearch/co-tracker/blob/main/demo.py) · [Colab Resmi](https://colab.research.google.com/github/facebookresearch/co-tracker/blob/master/notebooks/demo.ipynb) · [Halaman Paket](https://brone.ub.ac.id/mod/page/view.php?id=246059&forceview=1#P13)
- **Gambaran & Masalah**: Pelacak sering menganggap titik masih terlihat padahal benda sudah tertutup. Uji balik dapat mendeteksi ketidakcocokan lintasan, namun kesalahan sesaat perlu dibedakan dari oklusi nyata.
- **Mulai dari Kode**: Jalankan `python demo.py --grid_size 10` atau Colab resmi menggunakan model **`cotracker3_offline`**. Uji pada klip pendek **TAP-Vid DAVIS**.
- **Perangkat**: GPU Colab gratis disarankan (karena pelacakan dua arah); CPU bisa dicoba pada satu klip sangat pendek dengan sedikit titik.
- **Perbaikan yang Dibuat**:
  1. Jalankan CoTracker3 maju; untuk tiap titik, cari bingkai terakhir yang diprediksi masih terlihat dan ambil posisinya.
  2. Balik urutan bingkai dan lacak kembali dari posisi tersebut; ukur jarak piksel antara prediksi maju dan balik di tiap bingkai.
  3. Ubah status titik menjadi "tidak terlihat" jika jarak melewati ambang validasi pada **2 bingkai berturut-turut** (koordinat tetap pakai hasil maju).
- **Cara Uji & Pelaporan**: Pada klip TAP-Vid DAVIS & titik awal yang sama (secara *offline*), bandingkan prediksi asli, aturan ambang 1 bingkai, dan aturan 2 bingkai berturut-turut. Laporkan **Average Jaccard**, **akurasi status tertutup/oklusi**, dan **biaya inferensi**.

---

### P14 · XFeat — Sebaran Titik Fitur untuk Registrasi pada Anggaran Tetap
- **Info**: CVPR 2024 · Ringan · Dapat Dimulai di CPU
- **Tautan**: [Paper Asli](https://openaccess.thecvf.com/content/CVPR2024/papers/Potje_XFeat_Accelerated_Features_for_Lightweight_Image_Matching_CVPR_2024_paper.pdf) · [Repo GitHub](https://github.com/verlab/accelerated_features) · [Contoh Kode (`minimal_example.py`)](https://github.com/verlab/accelerated_features/blob/main/minimal_example.py) · [Halaman Paket](https://brone.ub.ac.id/mod/page/view.php?id=246059&forceview=1#P14)
- **Gambaran & Masalah**: Titik fitur berskor tinggi sering menumpuk pada satu area bertekstur padat sehingga estimasi homografi menjadi kurang akurat di area gambar lainnya.
- **Mulai dari Kode**: Jalankan `python minimal_example.py`, lalu uji satu pasang foto **HPatches** dengan `XFeat.detectAndCompute` (2.048 kandidat awal, maksimal 512 titik dicocokkan).
- **Perangkat**: CPU lokal atau Colab CPU (contoh resmi menonaktifkan CUDA).
- **Perbaikan yang Dibuat**:
  1. Ambil hingga **2.048 kandidat** titik fitur per gambar.
  2. Bagi gambar menjadi **kisi 4 × 4 (16 sel)**; ambil maksimal **32 titik berskor tertinggi** dari tiap sel.
  3. Jika total < 512, isi sisanya dengan titik terbaik yang belum terpilih secara global, lalu lakukan pencocokan dan estimasi homografi dengan aturan identik.
- **Cara Uji & Pelaporan**: Pada pasangan HPatches yang sama (dipisah untuk perubahan **sudut pandang** vs perubahan **pencahayaan**), bandingkan pemilihan 512 skor tertinggi global vs 512 berbasis kisi. Laporkan **galat proyeksi sudut**, **jumlah pasangan titik valid**, dan **waktu pemrosesan**.

---

### P15 · TimesFM *(Cadangan)* — Memilih Panjang Riwayat yang Cukup untuk Meramal
- **Info**: ICML 2024 · Cadangan · Inferensi
- **Tautan**: [Paper Asli](https://proceedings.mlr.press/v235/das24c.html) · [Repo GitHub](https://github.com/google-research/timesfm) · [Contoh Kode (`v1/README.md` · PyTorch)](https://github.com/google-research/timesfm/blob/master/v1/README.md) · [Halaman Paket](https://brone.ub.ac.id/mod/page/view.php?id=246059&forceview=1#P15)
- **Gambaran & Masalah**: Tidak semua deret waktu membutuhkan konteks sepanjang 512 titik; riwayat 128 atau 256 titik mungkin sudah cukup akurat dan lebih cepat.
- **Mulai dari Kode**: Gunakan API lama `TimesFm` (`timesfm[torch]==1.3.0`) dengan checkpoint `google/timesfm-1.0-200m-pytorch`. Jalankan `tfm.forecast()` pada deret dengan > 512 pengamatan dan horizon tetap.
- **Perangkat**: CPU lokal atau Colab CPU dengan `backend="cpu"` (atau `backend="gpu"` jika GPU Colab tersedia).
- **Perbaikan yang Dibuat**:
  1. Pilih **3 waktu historis** (jawabannya sudah diketahui sebelum uji); evaluasi panjang riwayat `128`, `256`, dan `512` pada ketiganya.
  2. Cari galat rata-rata terkecil, lalu pilih **panjang riwayat terpendek** yang galatnya **$\le 1,01 \times$ galat terkecil** (aturan toleransi 1%).
  3. Pakai panjang terpilih pada titik uji berikutnya.
- **Cara Uji & Pelaporan**: Bandingkan selalu `512`, panjang terbaik tetap dari data validasi, dan pemilihan adaptif berbasis aturan 1% pada 3 titik historis. Laporkan **MAE** atau **MASE**, **waktu prediksi uji saja**, dan **waktu total** (termasuk 3 percobaan pemilihan panjang).

---

## 9. Pengembangan Menuju Publikasi *(Opsional)*

Jika hasil eksperimen menjanjikan dan tim berminat mengembangkan naskah menuju publikasi:
1. Cari **dua karya terdekat** dengan ide perbaikan; jelaskan kesamaan, perbedaan mekanisme, dan celah yang masih dapat diuji.
2. Ulangi pengujian pada **dataset atau lingkungan kedua**; laporkan hasil berpasangan beserta ketidakpastiannya, serta kondisi kapan perbaikan membantu vs hilang efeknya.
3. Lengkapi tabel pembanding, uji komponen (ablasi), dan catatan eksperimen reproduksibel, lalu diskusikan klaim dengan dosen.

---

## 10. Checklist Aksi Awal Tim (Minggu 1)

- [x] Bentuk tim (3 orang: Raditya, Gibran, Sulthon) dan inventarisasi perangkat (**Google Colab GPU gratis**).
- [x] Tentukan pilihan paket (**P04 · SAM 2**) — lanjutkan rincian kerja di [BRIEFING_P04_SAM2.md](./BRIEFING_P04_SAM2.md).
- [x] Pastikan paket **P04** belum diambil tim lain di daftar Kelas A dan laporkan kode paket serta nama/NIM anggota ke **koordinator kelas**.
- [ ] Buka notebook contoh penulis di Colab, siapkan environment (FP32 jika tanpa BF16), dan verifikasi **1 contoh gambar + 1 titik berjalan**.
- [ ] Catat detail awal (commit repo `sam2`, versi pustaka, checkpoint `sam2_hiera_tiny.pt`, jenis GPU Colab) untuk bagian Metode.
- [ ] Susun dan kumpulkan draf **Tahap 1 · Pendahuluan** sebelum **Selasa, 1 Desember 2026 pukul 23.59 WIB** (lihat rincian di [TAHAP1_BREAKDOWN_PENDAHULUAN.md](./TAHAP1_BREAKDOWN_PENDAHULUAN.md)).
