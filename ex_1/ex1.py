import numpy as np

# פונקציה שממירה ממעלות לרדיאנים
def deg2rad(degrees):
    return degrees * np.pi / 180


angles_deg = [0, 1, 5, 10, 30, 45, 90, 180]

print("degrees,radians,sin,cos")

for deg in angles_deg:
    rad = deg2rad(deg)
    s = np.sin(rad)
    c = np.cos(rad)
    print(f"{deg},{rad},{s},{c}")