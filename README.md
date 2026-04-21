# 🚀 Prediksi Harga Bitcoin - Web App & Machine Learning

## 📌 Deskripsi

Aplikasi berbasis web untuk memprediksi harga Bitcoin menggunakan **Machine Learning (SVR)**.
Project ini mencakup proses lengkap mulai dari **data preprocessing, training model, hingga implementasi ke web (Flask)**.

---

## 📊 Machine Learning Notebook

Proses training dan analisis dapat dilihat di:

* `BITCOIN.ipynb`

Notebook ini berisi:

* Data preprocessing
* Feature engineering (lag, moving average, volatility)
* Training model SVR
* Evaluasi model

---

## ⚙️ Persyaratan

* Python 3.8+
* pip

---

## 📦 Instalasi

```bash
pip install -r requirements.txt
```

---

## 📁 Struktur Folder

```
BITCOIN_APP/
│
├── BITCOIN.ipynb   # Notebook Machine Learning
├── app.py          # Backend Flask
├── model.pkl       # Model hasil training
├── scaler.pkl      # Scaler fitur
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
```

---

## Cara Menjalankan Web

```bash
python app.py
```

Buka browser:

```
http://localhost:5050
```
---

## 🌐 Tampilan Web Aplikasi

### 🔹 Halaman Utama (Belum Input Data)
Halaman awal aplikasi sebelum pengguna memasukkan data prediksi.

![Halaman Utama](<img width="959" height="478" alt="Screenshot 2026-04-21 131805" src="https://github.com/user-attachments/assets/8184a63d-68f8-4913-88fc-686f5d460a57" />
)

---

### 🔹 Input Data
Pengguna memasukkan data fitur (lag, moving average, dll).  
Pada contoh ini digunakan **pilihan data ke-2** agar proses lebih cepat.

![Input Data](<img width="959" height="471" alt="Screenshot 2026-04-21 131942" src="https://github.com/user-attachments/assets/98ea765d-f18c-4820-9991-bf4c99377567" />
)

---

### 🔹 Hasil Prediksi
Menampilkan hasil prediksi harga Bitcoin berdasarkan input yang diberikan.

![Hasil Prediksi](<img width="958" height="474" alt="Screenshot 2026-04-21 132018" src="https://github.com/user-attachments/assets/b0227d3b-47b1-4e3f-b48e-68bf8486b8b0" />
)

---

## Fitur Input

| Fitur      | Keterangan                             |
| ---------- | -------------------------------------- |
| lag1       | Harga penutupan kemarin (t-1)          |
| lag2       | Harga penutupan 2 hari lalu (t-2)      |
| lag3       | Harga penutupan 3 hari lalu (t-3)      |
| ma5        | Moving average 5 hari terakhir         |
| ma10       | Moving average 10 hari terakhir        |
| ma20       | Moving average 20 hari terakhir        |
| std20      | Deviasi standar harga 20 hari terakhir |
| volatility | Nilai volatilitas harga                |

---

## Model Machine Learning

* **Algoritma:** Support Vector Regression (SVR)
* **Kernel:** Linear
* **Parameter terbaik:** C = 10
* **Scaler:** StandardScaler
* **Jumlah fitur:** 8

---

## Tujuan Project

* Memprediksi harga Bitcoin berdasarkan data historis
* Mengimplementasikan model ML ke dalam web app
* Memahami alur end-to-end Machine Learning

---

## Author

* Zakiatul Balqis
