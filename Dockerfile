FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Salin semua file ke dalam container
COPY . .

# Install dependencies sistem termasuk libGL
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && apt-get clean

# Atur variabel lingkungan untuk mengurangi warning TensorFlow
ENV TF_CPP_MIN_LOG_LEVEL=2

# Jalankan aplikasi dengan Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]