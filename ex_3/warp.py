import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

# =========================
# קריאת תמונה שתומכת בעברית
# =========================
def imread_unicode(path):
    stream = np.fromfile(path, dtype=np.uint8)
    return cv2.imdecode(stream, cv2.IMREAD_COLOR)

# =========================
# warp עם לולאות (bilinear)
# =========================
def warp_loop(img, angle, scale_x, scale_y):
    h, w = img.shape[:2]
    cx, cy = w / 2, h / 2
    theta = np.deg2rad(angle)

    T = np.array([
        [scale_x * np.cos(theta), -scale_y * np.sin(theta)],
        [scale_x * np.sin(theta),  scale_y * np.cos(theta)]
    ])
    T_inv = np.linalg.inv(T)

    out = np.zeros_like(img)

    for i in range(h):
        for j in range(w):
            x = j + 0.5 - cx
            y = i + 0.5 - cy

            src = T_inv @ np.array([x, y])

            x_src = src[0] + cx - 0.5
            y_src = src[1] + cy - 0.5

            if 0 <= x_src < w-1 and 0 <= y_src < h-1:
                x0 = int(np.floor(x_src))
                y0 = int(np.floor(y_src))

                dx = x_src - x0
                dy = y_src - y0

                for c in range(3):
                    out[i, j, c] = (
                        img[y0, x0, c] * (1 - dx) * (1 - dy) +
                        img[y0, x0+1, c] * dx * (1 - dy) +
                        img[y0+1, x0, c] * (1 - dx) * dy +
                        img[y0+1, x0+1, c] * dx * dy
                    )
    return out

# =========================
# warp עם numpy (nearest)
# =========================
def warp_numpy(img, angle, scale_x, scale_y):
    h, w = img.shape[:2]
    cx, cy = w / 2, h / 2
    theta = np.deg2rad(angle)

    T = np.array([
        [scale_x * np.cos(theta), -scale_y * np.sin(theta)],
        [scale_x * np.sin(theta),  scale_y * np.cos(theta)]
    ])
    T_inv = np.linalg.inv(T)

    j, i = np.meshgrid(np.arange(w), np.arange(h))

    x = j + 0.5 - cx
    y = i + 0.5 - cy

    coords = np.stack([x, y], axis=0).reshape(2, -1)
    src = T_inv @ coords

    x_src = src[0].reshape(h, w) + cx - 0.5
    y_src = src[1].reshape(h, w) + cy - 0.5

    x_nn = np.round(x_src).astype(int)
    y_nn = np.round(y_src).astype(int)

    out = np.zeros_like(img)

    valid = (x_nn >= 0) & (x_nn < w) & (y_nn >= 0) & (y_nn < h)

    out[valid] = img[y_nn[valid], x_nn[valid]]

    return out

# =========================
# GUI
# =========================
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Affine Transform")

        # בחירת תמונה (תומך בעברית)
        path = filedialog.askopenfilename(title="בחרי תמונה")
        if not path:
            print("לא נבחרה תמונה")
            exit()

        self.img = imread_unicode(path)
        if self.img is None:
            print("שגיאה בטעינת התמונה")
            exit()

        self.method = "numpy"

        self.angle = tk.DoubleVar()
        self.scale_x = tk.DoubleVar(value=1.0)
        self.scale_y = tk.DoubleVar(value=1.0)

        tk.Scale(root, from_=-180, to=180, orient="horizontal",
                 label="Rotation", variable=self.angle,
                 command=self.update).pack(fill="x")

        tk.Scale(root, from_=0.1, to=2.0, resolution=0.1,
                 orient="horizontal", label="Scale X",
                 variable=self.scale_x,
                 command=self.update).pack(fill="x")

        tk.Scale(root, from_=0.1, to=2.0, resolution=0.1,
                 orient="horizontal", label="Scale Y",
                 variable=self.scale_y,
                 command=self.update).pack(fill="x")

        tk.Button(root, text="Load Image", command=self.load_image).pack()
        tk.Button(root, text="Switch Method", command=self.switch_method).pack()

        self.update()

    def load_image(self):
        path = filedialog.askopenfilename(title="בחרי תמונה")
        if path:
            self.img = imread_unicode(path)
            self.update()

    def switch_method(self):
        self.method = "loop" if self.method == "numpy" else "numpy"
        print("Method:", self.method)
        self.update()

    def update(self, event=None):
        angle = self.angle.get()
        sx = self.scale_x.get()
        sy = self.scale_y.get()

        if self.method == "loop":
            out = warp_loop(self.img, angle, sx, sy)
        else:
            out = warp_numpy(self.img, angle, sx, sy)

        cv2.imshow("Original", self.img)
        cv2.imshow("Transformed", out)
        cv2.waitKey(1)
        import time

def measure_time(func, img, name):
    start = time.time()
    func(img, 30, 1.2, 1.2)
    end = time.time()
    return end - start

def run_benchmark():
    sizes = [(256,256), (512,512), (1024,1024)]

    print("\nגובה | רוחב | זמן לולאות | זמן numpy")
    print("---------------------------------------")

    for h, w in sizes:
        img = np.random.randint(0,255,(h,w,3),dtype=np.uint8)

        t_loop = measure_time(warp_loop, img, "loop")
        t_numpy = measure_time(warp_numpy, img, "numpy")

        print(f"{h:5} | {w:5} | {t_loop:.4f} | {t_numpy:.4f}")

# =========================
# הרצה
# =========================
root = tk.Tk()
app = App(root)
root.mainloop()
cv2.destroyAllWindows()