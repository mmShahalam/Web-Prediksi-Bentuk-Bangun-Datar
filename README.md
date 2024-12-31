# Web Prediksi Bentuk Bangun Datar

## 📖 Overview
Merupakan aplikasi web berbasis **Flask** yang menggunakan **Convolutional Neural Network (CNN)** untuk memprediksi bentuk geometris dari gambar yang diunggah pengguna.

## ✨ Features
- **Upload Gambar**: Pengguna dapat mengunggah gambar bentuk geometris.
- **Prediksi Akurat**: Aplikasi menggunakan model CNN terlatih untuk mengklasifikasikan gambar ke dalam 17 kategori bentuk, seperti lingkaran, segitiga, persegi, bintang, dan lainnya.
- **Antarmuka Sederhana**: UI yang user-friendly dengan navigasi yang mudah.
- **Cepat dan Ringan**: Dirancang untuk memberikan hasil dalam waktu singkat.

## 🛠️ Technologies Used
- Python: Logika backend dan integrasi model.
- Flask: Framework web untuk membuat aplikasi.
- TensorFlow: Framework untuk melatih dan mendistribusikan model CNN.
- OpenCV: Untuk preprocessing gambar.
- Gunicorn: WSGI server untuk deployment di lingkungan produksi.

## 🌐 Deployment
Aplikasi ini dideploy menggunakan Railway. Anda dapat mengakses aplikasi yang sudah berjalan di URL berikut: [URL Web](https://web-prediksi-bentuk-bangun-datar.up.railway.app/)

## 📊 Model Details
- Model Architecture: Convolutional Neural Network (CNN) dengan 2 convolutional layers, max pooling, dan fully connected layers.
- Input Size: 64x64 grayscale images.
- Classes: Circle, Decagon, Heptagon, Hexagon, Kite, Nonagon, Octagon, Oval, Parallelogram, Pentagon, Rectangle, Rhombus, Semicircle, Square, Star, Trapezoid, Triangle.

##🖼️ Screenshots
- Home Page
![Home Page](https://github.com/user-attachments/assets/0cc5550d-be96-4768-99ca-28fd9e7c1a0a)

- Prediction Result
![Result](https://github.com/user-attachments/assets/82d4cec0-360f-4e61-b140-5c49984ac2f8)

## 👨‍💻 Author
- **Muhammad Mirza Shah Alam**: [GitHub Profile](https://github.com/mmShahalam)
