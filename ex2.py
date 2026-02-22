import numpy as np

# -------------------------
# מטריצת סיבוב כללית
# -------------------------
def rotation_matrix(theta_rad):
    return np.array([
        [np.cos(theta_rad), -np.sin(theta_rad)],
        [np.sin(theta_rad),  np.cos(theta_rad)]
    ])


# דוגמה: סיבוב 30 מעלות
theta = 30 * np.pi / 180
r_30 = rotation_matrix(theta)

print("Rotation matrix (30 degrees):")
print(r_30)


# -------------------------
# scale פי 2 בכל הכיוונים
# -------------------------
scale_all = np.array([
    [2, 0],
    [0, 2]
])

print("\nScale x2 in both directions:")
print(scale_all)


# -------------------------
# scale פי 2 בציר x בלבד
# -------------------------
scale_x = np.array([
    [2, 0],
    [0, 1]
])

print("\nScale x2 in x direction:")
print(scale_x)