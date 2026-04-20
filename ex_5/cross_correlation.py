import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from scipy.signal import correlate2d


# א. יצירת kernel
def initialize_kernel():
    kernel = np.array([
        [-1, 2, 1],
        [-2, 1, -3],
        [3, 0, -1]
    ], dtype=np.float32)
    return kernel


# ב. יצירת תמונה
def get_image():
    image = np.array([
        [103, 102, 101, 100],
        [104, 103, 102, 101],
        [53,  52,  51,  50],
        [45,  53,  52,  51]
    ], dtype=np.uint8)
    return image


# ג. מימוש עם לולאות
def cross_correlate_loop(image, kernel):
    h, w = image.shape
    k = kernel.shape[0]

    out_h = h - k + 1
    out_w = w - k + 1

    result = np.zeros((out_h, out_w), dtype=np.float32)

    for i in range(out_h):
        for j in range(out_w):
            patch = image[i:i+k, j:j+k]
            result[i, j] = np.sum(patch * kernel)

    return result


# ד. מימוש עם numpy
def cross_correlate_np(image, kernel):
    k = kernel.shape[0]

    windows = sliding_window_view(image, (k, k))
    result = np.sum(windows * kernel, axis=(2, 3)).astype(np.float32)

    return result


# ה. מימוש עם scipy
def cross_correlate_scipy(image, kernel):
    result = correlate2d(image, kernel, mode='valid')
    return result.astype(np.float32)


# ו. השוואה
def compare_cross_correlations():
    image = get_image()
    kernel = initialize_kernel()

    r1 = cross_correlate_loop(image, kernel)
    r2 = cross_correlate_np(image, kernel)
    r3 = cross_correlate_scipy(image, kernel)

    return np.allclose(r1, r2) and np.allclose(r1, r3)


if __name__ == "__main__":
    print("Loop result:\n", cross_correlate_loop(get_image(), initialize_kernel()))
    print("NumPy result:\n", cross_correlate_np(get_image(), initialize_kernel()))
    print("SciPy result:\n", cross_correlate_scipy(get_image(), initialize_kernel()))
    print("All equal:", compare_cross_correlations())