import numpy as np
import cv2
import matplotlib.pyplot as plt

def create_gradient_image(height, width):
    img = np.zeros((height, width), dtype=np.uint8)
    max_sum = (height - 1) + (width - 1)
    for r in range(height):
        for c in range(width):
            img[r, c] = int((r + c) * 255 / max_sum)
    return img

def brighten(img, b, func):
    if func == "np":
        return np.add(img, b)
    elif func == "cv2":
        return cv2.add(img, b)
    else:
        raise ValueError("func must be 'np' or 'cv2'")

img = create_gradient_image(300, 300)

img_np = brighten(img, 80, "np")
img_cv = brighten(img, 80, "cv2")

plt.subplot(1,2,1)
plt.imshow(img_np, cmap='gray')
plt.title("np.add")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(img_cv, cmap='gray')
plt.title("cv2.add")
plt.axis('off')

plt.show()
