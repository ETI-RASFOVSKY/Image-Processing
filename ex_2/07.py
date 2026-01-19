import numpy as np
import matplotlib.pyplot as plt


# פונקציה לחישוב היסטוגרמה
def compute_histogram(img):
    hist = np.zeros(256, dtype=int)
    h, w = img.shape
    for r in range(h):
        for c in range(w):
            hist[img[r,c]] += 1
    return hist

# --- יוצרים תמונה לדוגמה ---
# אפשר תמונת גרדיאנט:
def create_gradient_image(height, width):
    img = np.zeros((height, width), dtype=np.uint8)
    max_sum = (height - 1) + (width - 1)
    for r in range(height):
        for c in range(width):
            img[r, c] = int((r + c) * 255 / max_sum)
    return img

img = create_gradient_image(300, 300)

# --- עכשיו מחשבים היסטוגרמה ---
hist = compute_histogram(img)

# --- מציגים גרף ---
plt.bar(range(256), hist)
plt.title("Histogram")
plt.xlabel("Gray level")
plt.ylabel("Count")
plt.show()
