import numpy as np
import matplotlib.pyplot as plt

def create_gradient_image(height, width):
    img = np.zeros((height, width), dtype=np.uint8)

    max_sum = (height - 1) + (width - 1)

    for r in range(height):
        for c in range(width):
            img[r, c] = int((r + c) * 255 / max_sum)

    return img

img = create_gradient_image(300, 300)

plt.imshow(img, cmap='gray')
plt.axis('off')
plt.show()
