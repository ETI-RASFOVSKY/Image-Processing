import sys
import cv2
import numpy as np
import os


def normalize_image(img):
    img = img.astype(np.float32)
    img = img - np.min(img)
    img = img / (np.max(img) + 1e-8)
    img = (img * 255).astype(np.uint8)
    return img


def main():
    if len(sys.argv) < 2:
        print("Usage: python sobel.py image.jpg")
        return

    image_path = sys.argv[1]

    # קריאה
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Sobel kernels
    gx_kernel = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ], dtype=np.float32)

    gy_kernel = np.array([
        [-1, -2, -1],
        [0,  0,  0],
        [1,  2,  1]
    ], dtype=np.float32)

    # חישוב
    gx = cv2.filter2D(gray.astype(np.float32), -1, gx_kernel)
    gy = cv2.filter2D(gray.astype(np.float32), -1, gy_kernel)

    magnitude = np.sqrt(gx**2 + gy**2)

    # ערך מוחלט
    gx = np.abs(gx)
    gy = np.abs(gy)

    # נורמליזציה
    gx = normalize_image(gx)
    gy = normalize_image(gy)
    magnitude = normalize_image(magnitude)

    # שמירה
    base, ext = os.path.splitext(image_path)

    cv2.imwrite(base + "_grayscale" + ext, gray)
    cv2.imwrite(base + "_gx" + ext, gx)
    cv2.imwrite(base + "_gy" + ext, gy)
    cv2.imwrite(base + "_magnitude" + ext, magnitude)

    print("Done!")


if __name__ == "__main__":
    main()