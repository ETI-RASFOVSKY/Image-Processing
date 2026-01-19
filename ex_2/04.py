import matplotlib.pyplot as plt
import numpy as np
import cv2
def create_low_contrast_image(height, width, bg, fg):
    img = np.full((height, width), bg, dtype=np.uint8)

    center = (width // 2, height // 2)
    radius = min(height, width) // 4

    cv2.circle(img, center, radius, fg, -1)

    return img
def normalize_image(src):
    min_val = src.min()
    max_val = src.max()
    mean_val = src.mean()

    factor = 255 / (max_val - min_val)

    src_float = src.astype(np.float32)
    dst_float = (src_float - min_val) * factor

    dst = np.clip(dst_float, 0, 255).astype(np.uint8)

    return dst, min_val, max_val, mean_val, factor



# img = create_low_contrast_image(300, 300, 100, 105)

# plt.imshow(img, cmap='gray')
# plt.axis('off')
# plt.show()


low_contrast = create_low_contrast_image(300, 300, 100, 105)
norm_img, mn, mx, mean, f = normalize_image(low_contrast)

print("min:", mn, "max:", mx, "mean:", mean)
print("stretch factor:", f)

test_img = low_contrast.copy()
test_img[0,0] = 0
test_img[0,1] = 255

norm_extreme, mn, mx, _, _ = normalize_image(test_img)

