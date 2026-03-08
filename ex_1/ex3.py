import numpy as np
import matplotlib.pyplot as plt

# -------------------------
# פונקציה המרה לרדיאנים
# -------------------------
def deg2rad(degrees):
    return degrees * np.pi / 180


# -------------------------
# מטריצת סיבוב 30 מעלות
# -------------------------
theta = deg2rad(30)

r_30 = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta),  np.cos(theta)]
])

print("r_30 =\n", r_30)


# -------------------------
# מטריצת מתיחה פי 2 בציר x
# -------------------------
sx_2 = np.array([
    [2, 0],
    [0, 1]
])

print("\nsx_2 =\n", sx_2)


# -------------------------
# חישוב rs ו-sr
# -------------------------
rs = r_30 @ sx_2
sr = sx_2 @ r_30

print("\nrs =\n", rs)
print("\nsr =\n", sr)


# -------------------------
# יצירת מלבן (רוחב 2, גובה 1)
# -------------------------
rectangle = np.array([
    [-1, -0.5],
    [ 1, -0.5],
    [ 1,  0.5],
    [-1,  0.5],
    [-1, -0.5]
])


# -------------------------
# טרנספורמציות
# -------------------------
rotated_rect = (r_30 @ rectangle.T).T
scaled_rect  = (sx_2 @ rectangle.T).T
rect_rs      = (rs @ rectangle.T).T
rect_sr      = (sr @ rectangle.T).T


# -------------------------
# ציור
# -------------------------
plt.figure()

plt.plot(rectangle[:,0], rectangle[:,1], label="original")
plt.plot(rotated_rect[:,0], rotated_rect[:,1], label="rotated 30°")
plt.plot(scaled_rect[:,0], scaled_rect[:,1], label="scale x2")
plt.plot(rect_rs[:,0], rect_rs[:,1], label="r_30 @ sx_2")
plt.plot(rect_sr[:,0], rect_sr[:,1], label="sx_2 @ r_30")

plt.legend()
plt.axis("equal")
plt.title("Rotation and Scaling Transformations")
plt.show()