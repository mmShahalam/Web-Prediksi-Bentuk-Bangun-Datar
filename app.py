import os
from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
import cv2
import numpy as np

app = Flask(__name__)
model = load_model("shape_classifier.h5")

# Folder untuk menyimpan file yang diunggah
UPLOAD_FOLDER = "static/uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Daftar kategori
categories = [
    "Circle", "Decagon", "Heptagon", "Hexagon", "Kite", "Nonagon",
    "Octagon", "Oval", "Parallelogram", "Pentagon", "Rectangle",
    "Rhombus", "Semicircle", "Square", "Star", "Trapezoid", "Triangle"
]

def preprocess_image(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (64, 64)) / 255.0
    return img.reshape(1, 64, 64, 1)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/classify", methods=["POST"])
def classify():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file:
        # Simpan file ke folder uploads
        img_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(img_path)

        # Preprocess gambar dan prediksi
        img = preprocess_image(img_path)
        prediction = model.predict(img)
        result = categories[np.argmax(prediction)]

        # Kirim hasil prediksi dan path gambar relatif
        return jsonify({"result": result, "image_path": "/" + img_path})
    return jsonify({"error": "File upload failed"}), 500

if __name__ == "__main__":
    app.run(debug=True)