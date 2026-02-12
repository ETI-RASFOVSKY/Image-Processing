import cv2
import numpy as np
import sys

def manual_conversions(r, g, b):
    # נרמול לטווח [0, 1]
    rf, gf, bf = r / 255.0, g / 255.0, b / 255.0
    cmax = max(rf, gf, bf)
    cmin = min(rf, gf, bf)
    diff = cmax - cmin

    # --- HSV Calculation ---
    # Hue
    if diff == 0: h = 0
    elif cmax == rf: h = (60 * ((gf - bf) / diff) + 360) % 360
    elif cmax == gf: h = (60 * ((bf - rf) / diff) + 120) % 360
    elif cmax == bf: h = (60 * ((rf - gf) / diff) + 240) % 360
    # Saturation & Value
    s_hsv = 0 if cmax == 0 else (diff / cmax) * 100
    v = cmax * 100
    
    # --- HSL Calculation ---
    l = (cmax + cmin) / 2
    s_hsl = 0 if diff == 0 else (diff / (1 - abs(2 * l - 1))) * 100
    l *= 100
    
    # --- YCrCb Calculation (BT.601) ---
    y = 0.299 * r + 0.587 * g + 0.114 * b
    cr = (r - y) * 0.713 + 128
    cb = (b - y) * 0.564 + 128
    
    return (h/2, s_hsv*2.55, v*2.55), (h/2, s_hsl*2.55, l*2.55), (y, cr, cb)

def opencv_conversions(r, g, b):
    # OpenCV מצפה למערך Numpy בפורמט BGR
    pixel = np.array([[[b, g, r]]], dtype=np.uint8)
    
    hsv = cv2.cvtColor(pixel, cv2.COLOR_BGR2HSV)[0][0]
    # הערה: ל-OpenCV אין המרת BGR2HSL ישירה ב-uint8, משתמשים ב-HLS
    hls = cv2.cvtColor(pixel, cv2.COLOR_BGR2HLS)[0][0]
    ycrcb = cv2.cvtColor(pixel, cv2.COLOR_BGR2YCrCb)[0][0]
    
    return hsv, hls, ycrcb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <R> <G> <B>")
        sys.exit(1)
        
    r, g, b = map(int, sys.argv[1:])
    
    manual = manual_conversions(r, g, b)
    auto = opencv_conversions(r, g, b)
    
    models = ["HSV", "HSL/HLS", "YCrCb"]
    for i, model in enumerate(models):
        print(f"--- {model} ---")
        print(f"Manual: {manual[i]}")
        print(f"OpenCV: {auto[i]}")