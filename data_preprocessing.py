import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split

def load_data(data_dir):
    images = []
    labels = []

    # Update daftar kategori
    categories = [
        'circle', 'decagon', 'heptagon', 'hexagon', 'kite', 'nonagon',
        'octagon', 'oval', 'parallelogram', 'pentagon', 'rectangle',
        'rhombus', 'semicircle', 'square', 'star', 'trapezoid', 'triangle'
    ]
    label_map = {cat: i for i, cat in enumerate(categories)}

    for category in categories:
        folder_path = os.path.join(data_dir, category)
        for img_name in os.listdir(folder_path):
            img_path = os.path.join(folder_path, img_name)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (64, 64))  # Resize to 64x64
            images.append(img)
            labels.append(label_map[category])

    images = np.array(images) / 255.0  # Normalize pixel values
    labels = np.array(labels)
    return train_test_split(images, labels, test_size=0.2, random_state=42)

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = load_data("dataset")
    np.save("X_train.npy", X_train)
    np.save("X_test.npy", X_test)
    np.save("y_train.npy", y_train)
    np.save("y_test.npy", y_test)