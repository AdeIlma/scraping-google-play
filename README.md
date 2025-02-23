# Scraping Ulasan Aplikasi Google Play Store dengan Python & Streamlit

## 📌 Deskripsi
Proyek ini memungkinkan pengguna untuk mengambil ulasan aplikasi dari **Google Play Store** menggunakan **google-play-scraper** dan menampilkannya dalam aplikasi **Streamlit**. Ulasan yang diambil dapat difilter berdasarkan **rentang tanggal**, dan hasilnya dapat diunduh dalam format **CSV atau Excel**.

## 🚀 Fitur
- Scraping ulasan dari **Google Play Store** berdasarkan ID aplikasi.
- Menentukan jumlah maksimum ulasan yang diambil.
- Filter ulasan berdasarkan **rentang tanggal**.
- Menampilkan hasil scraping dalam **tabel interaktif**.
- Opsi untuk **mengunduh data dalam format CSV atau Excel**.

## 📦 Instalasi
Pastikan Anda sudah menginstal **Python** dan memiliki **pip**.

1. **Clone repositori ini** (atau buat file `.py` dengan kode yang sesuai):
   ```sh
   git clone https://github.com/username/repo-name.git
   cd repo-name
   ```

2. **Buat dan aktifkan virtual environment (opsional tapi disarankan)**:
   ```sh
   python -m venv env
   source env/bin/activate  # Untuk macOS/Linux
   env\Scripts\activate  # Untuk Windows
   ```

3. **Instal dependensi yang diperlukan**:
   ```sh
   pip install -r requirements.txt
   ```

## 🛠 Teknologi yang Digunakan
- **Python** (Versi 3.x)
- **Streamlit** (Untuk UI aplikasi web)
- **Google Play Scraper** (Untuk mengambil ulasan dari Google Play)
- **Pandas** (Untuk pengolahan data)
- **OpenPyXL** (Untuk ekspor ke Excel)

## 🎯 Cara Menjalankan Aplikasi
1. **Jalankan Streamlit**
   ```sh
   streamlit run app.py
   ```
2. **Buka di browser**:
   - **http://localhost:8501**

## 📝 Penggunaan
1. Masukkan **jumlah aplikasi** yang ingin diambil ulasannya.
2. Isi **ID aplikasi** (contoh: `com.gojek.gopay`).
3. Masukkan **nama aplikasi** untuk referensi.
4. Tentukan **jumlah ulasan maksimal** yang ingin diambil.
5. Pilih **rentang tanggal** untuk memfilter ulasan.
6. Klik tombol **"Mulai Pengambilan Ulasan"**.
7. Tunggu hingga proses selesai, lalu unduh hasilnya dalam **CSV atau Excel**.

## 📂 Struktur Proyek
```
.
├── app.py  # File utama untuk aplikasi Streamlit
├── requirements.txt  # Daftar pustaka yang dibutuhkan
├── README.md  # Dokumentasi proyek
└── data/  # (Opsional) Folder untuk menyimpan data hasil scraping
```

## 🛠 Dependencies (requirements.txt)
Berikut adalah pustaka yang perlu diinstal untuk menjalankan proyek ini:
```
streamlit
pandas
google-play-scraper
openpyxl
```

## 📌 Catatan
- Pastikan ID aplikasi yang dimasukkan sesuai dengan format Google Play Store (contoh: `com.gojek.gopay`).
- Jika **scraping berhenti tiba-tiba**, tunggu beberapa saat dan coba lagi (untuk menghindari rate limiting dari Google Play Store).
- Gunakan **virtual environment** agar tidak mengganggu pustaka yang terinstal di sistem.

## 💡 Lisensi
Proyek ini bersifat **open-source** dan dapat digunakan untuk keperluan non-komersial.

## 🙌 Kontribusi
Jika ingin berkontribusi dalam pengembangan proyek ini:
1. **Fork repositori ini**
2. **Buat branch baru** (`git checkout -b fitur-baru`)
3. **Commit perubahan** (`git commit -m "Menambahkan fitur X"`)
4. **Push ke branch** (`git push origin fitur-baru`)
5. **Buat Pull Request**

🚀 Selamat mencoba dan semoga bermanfaat!

