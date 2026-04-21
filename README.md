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

> ⚠️ Jika terjadi konflik versi:

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac
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

## ▶️ Cara Menjalankan Web

```bash
python app.py
```

Buka browser:

```
http://localhost:5050
```

---

## 🧾 Fitur Input

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

## 🤖 Model Machine Learning

* **Algoritma:** Support Vector Regression (SVR)
* **Kernel:** Linear
* **Parameter terbaik:** C = 10
* **Scaler:** StandardScaler
* **Jumlah fitur:** 8

---

## 🎯 Tujuan Project

* Memprediksi harga Bitcoin berdasarkan data historis
* Mengimplementasikan model ML ke dalam web app
* Memahami alur end-to-end Machine Learning

---

## 👩‍💻 Author

* Zakiatul Balqis
