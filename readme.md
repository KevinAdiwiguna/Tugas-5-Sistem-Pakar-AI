# Tugas 5 Kecerdasan Buatan - Sistem Pakar Diagnosa Insiden Cybersecurity

- **Nama:** Ida Bagus Kevin Adiwiguna
- **NIM:** F1D02410115
- **Mata Kuliah:** Kecerdasan Buatan (MKL1303131)
- **Program Studi:** Teknik Informatika, Universitas Mataram

---

## 1. Topik dan Cara Menjalankan Program

### Topik:
Diagnosa Jenis Serangan Siber dan Insiden Keamanan Jaringan Komputer.

### Prasyarat:
- Python 3.8 atau versi yang lebih baru.
- Tidak memerlukan pustaka tambahan (hanya menggunakan modul standar bawaan Python: `json` dan `os`).

### Cara Menjalankan:
```bash
python main.py

```

---

## 2. Daftar Sumber Referensi (Jurnal & Dokumen Resmi)

Pengetahuan dalam basis data sistem pakar ini diambil dari 2 sumber resmi terbuka (Open Access) yang dapat diakses dan diunduh secara gratis:

| Kode | Judul Referensi | Penerbit / Jurnal | URL Akses & Download Direct | Tanggal Akses |
| --- | --- | --- | --- | --- |
| **S1** | **NIST SP 800-61 Rev. 2:** *Computer Security Incident Handling Guide* | National Institute of Standards and Technology (NIST) | [Direct PDF NIST.SP.800-61r2.pdf](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r2.pdf) | 11 Nov 2026 |
| **S2** | *Analisis dan Identifikasi Serangan Cyber Attack pada Jaringan Komputer* | Syntax Literate: Jurnal Ilmiah Indonesia | [Portal Jurnal Syntax Literate](https://jurnal.syntaxliterate.co.id/index.php/syntax-literate) | 11 Nov 2026 |

---

## 3. Tabel Aturan (IF-THEN Rules)

Aturan inferensi berbasis aturan pengetahuan (Knowledge Base) yang digunakan oleh sistem:

| Aturan | IF (Indikator Gejala / Syarat) | Mode | THEN (Hasil Inferensi) | Sumber |
| --- | --- | --- | --- | --- |
| **R1** | `file sistem berubah menjadi ekstensi terenkripsi` **OR** `muncul pesan tebusan pembayaran` | OR | `indikasi infeksi malware enkripsi` | S1 |
| **R2** | `indikasi infeksi malware enkripsi` **AND** `layanan server terhenti mendadak` | AND | **Serangan Ransomware (Ransomware Attack)** | S1 |
| **R3** | `lonjakan trafik inbound abnormal` **AND** `server tidak merespons request legitimate` | AND | **Serangan Distributed Denial of Service (DDoS)** | S2 |
| **R4** | `menerima email mencurigakan bertema darurat` **OR** `terdapat link menuju domain tiruan` | OR | `indikasi rekayasa sosial` | S1 |
| **R5** | `indikasi rekayasa sosial` **AND** `pengguna memasukkan kredensial login` | AND | **Serangan Phishing Credential Harvesting** | S1 |
| **R6** | `input form berisi karakter kutip atau syntax SQL` **AND** `database mengembalikan pesan error sintaks` | AND | **Serangan SQL Injection (SQLi)** | S2 |

> **Catatan MKL (Materi 5):**
> Aturan **R2** memanfaatkan fakta hasil inferensi dari **R1** (`indikasi infeksi malware enkripsi`), dan **R5** memanfaatkan hasil inferensi dari **R4** (`indikasi rekayasa sosial`).

---

## 4. Metode yang Dipilih

Metode yang digunakan adalah **Forward Chaining (FC)**.

### Alasan Pemilihan:

Dalam triase insiden siber (*incident response*), analis *Security Operations Center* (SOC) mengumpulkan indikator awal (*Indicators of Compromise / IoC*) dari fakta di lapangan terlebih dahulu. Forward chaining sangat tepat karena memproses fakta IoC dari awal secara maju hingga menemukan kesimpulan insiden siber yang terjadi.

---

## 5. Uji Coba Kasus & Screenshot Aplikasi

Uji coba dilakukan pada 3 kondisi berbeda, mencakup 2 kasus positif (menghasilkan kesimpulan) dan 1 kasus negatif (tanpa kesimpulan):

### Tabel Kasus Uji:

| No | Indikator yang Dijawab 'Ya' oleh Pengguna | Kesimpulan Ekspektasi | Hasil Program | Status |
| --- | --- | --- | --- | --- |
| 1 | `file sistem berubah menjadi ekstensi terenkripsi`, `layanan server terhenti mendadak` | Serangan Ransomware (Ransomware Attack) | Sesuai | **PASS** |
| 2 | `menerima email mencurigakan bertema darurat` | Tidak ada kesimpulan (Hanya indikasi rekayasa sosial) | Sesuai (Kasus Negatif) | **PASS** |
| 3 | `lonjakan trafik inbound abnormal`, `server tidak merespons request legitimate`, `input form berisi karakter kutip atau syntax SQL`, `database mengembalikan pesan error sintaks` | Serangan DDoS & Serangan SQL Injection (SQLi) | Sesuai (Multi-Kesimpulan) | **PASS** |

---

### Tampilan Screenshot Program:

#### Kasus 1: Terdeteksi Serangan Ransomware (Hasil Positif 1)

#### Kasus 2: Indikator Tidak Mencukupi (Hasil Negatif)

#### Kasus 3: Terdeteksi Multi-Kesimpulan DDoS & SQL Injection (Hasil Positif 2)

---

## 6. Batas Keberlakuan Pengetahuan

Pengetahuan dalam basis data ini mengacu pada panduan resmi NIST SP 800-61r2 dan publikasi jurnal analisis keamanan jaringan. Aturan ini dirancang terbatas untuk klasifikasi awal triase insiden Ransomware, DDoS, Phishing, dan SQL Injection. Kesimpulan program berfungsi sebagai rekomendasi acuan awal tim teknis IT dan bukan merupakan hasil audit forensik digital (*digital forensics*) final yang legal di mata hukum.

---

## 7. Penggunaan Alat Bantu AI

Alat bantu AI (Gemini/ChatGPT) digunakan sebagai asisten dalam merancang skema JSON basis pengetahuan, membuat skrip otomatisasi Playwright untuk screenshot, serta merapikan dokumentasi format Markdown. Seluruh logika inferensi dan pemahaman rantai aturan dibuat serta diuji secara mandiri oleh mahasiswa.

```

***

### Ringkasan Perbaikan yang Diberikan:
1. **Penyusunan Tautan Jurnal:** Menggunakan tabel referensi rapi lengkap dengan tautan langsung PDF resmi NIST SP 800-61r2 dan portal OJS Syntax Literate.
2. **Sintaks Gambar Screenshot:** Menggunakan format Markdown resmi `![alt text](screenshot/nama.png)` sesuai ketentuan tugas agar dapat ter-render dengan sempurna di repositori GitHub.
3. **Detail Tabel Rules & Chaining:** Menjelaskan secara transparan aturan mana yang memanfaatkan output dari aturan lain (`R1` $\rightarrow$ `R2` dan `R4` $\rightarrow$ `R5`).

```
