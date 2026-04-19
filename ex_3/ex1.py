import numpy as np
import cv2
import matplotlib.pyplot as plt
import os



# -----------------------------
# אינטרפולציה בילינארית
# -----------------------------
def bilinear_interpolation(img, x, y):
    h, w = img.shape[:2]

    if x < 0 or x >= w-1 or y < 0 or y >= h-1:
        return 0

    x0 = int(np.floor(x))
    x1 = x0 + 1
    y0 = int(np.floor(y))
    y1 = y0 + 1

    dx = x - x0
    dy = y - y0

    val = (1-dx)*(1-dy)*img[y0, x0] + \
          dx*(1-dy)*img[y0, x1] + \
          (1-dx)*dy*img[y1, x0] + \
          dx*dy*img[y1, x1]

    return val


# -----------------------------
# הפונקציה הראשית של התרגיל
# -----------------------------
def warp_image(img, angle_deg, scale_x, scale_y):
    h, w = img.shape[:2]
    output = np.zeros_like(img)

    cx = w / 2
    cy = h / 2

    theta = np.deg2rad(angle_deg)

    # מטריצת טרנספורמציה
    T = np.array([
        [scale_x * np.cos(theta), -scale_y * np.sin(theta)],
        [scale_x * np.sin(theta),  scale_y * np.cos(theta)]
    ])

    # הופכי ל-backward mapping
    T_inv = np.linalg.inv(T)

    for i in range(h):
        for j in range(w):

            # מרכז פיקסל
            x = j + 0.5
            y = i + 0.5

            # הזזה למרכז
            x_shift = x - cx
            y_shift = y - cy

            # טרנספורמציה הפוכה
            src = T_inv @ np.array([x_shift, y_shift])

            # חזרה למערכת המקורית
            src_x = src[0] + cx - 0.5
            src_y = src[1] + cy - 0.5

            # אינטרפולציה
            if len(img.shape) == 3:
                for c in range(3):
                    output[i, j, c] = bilinear_interpolation(img[:,:,c], src_x, src_y)
            else:
                output[i, j] = bilinear_interpolation(img, src_x, src_y)

    return output.astype(np.uint8)


# -----------------------------
# קוד הרצה לבדיקה
# -----------------------------
if __name__ == "__main__":

    # טען תמונה (שימי קובץ בשם input.jpg בתיקייה)
    img = cv2.imread(r"C:\Users\PC\Desktop\תואר\Image-Processing\Semester B\ex_3\input.png")
    print(os.getcwd())

    if img is None:
        print("❌ לא נמצאה תמונה בשם input.png")
        exit()

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # פרמטרים לבדיקה
    angle = 30
    scale_x = 1.5
    scale_y = 0.7

    # הפעלת הטרנספורמציה
    result = warp_image(img, angle, scale_x, scale_y)

    # הצגה
    plt.figure(figsize=(10,5))

    plt.subplot(1,2,1)
    plt.title("Original")
    plt.imshow(img)
    plt.axis('off')

    plt.subplot(1,2,2)
    plt.title("Transformed")
    plt.imshow(result)
    plt.axis('off')

    plt.show()