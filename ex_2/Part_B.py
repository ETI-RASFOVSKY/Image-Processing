import numpy as np
import matplotlib.pyplot as plt


# פונקציית סיבוב
def rotation_matrix(theta):

    theta = np.radians(theta)

    R = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0,0,1]
    ])

    print("Rotation matrix:", theta)
    print(R)
    print()

    return R


# פונקציית מתיחה בציר x
def scale_x_matrix(s):

    S = np.array([
        [s,0,0],
        [0,1,0],
        [0,0,1]
    ])

    print("Scale matrix x:", s)
    print(S)
    print()

    return S


# ציור מלבן
def draw_rectangle(points, label):

    plt.plot(points[:,0], points[:,1], label=label)


# מלבן שמרכזו בראשית
rectangle = np.array([
    [-1,-0.5,1],
    [ 1,-0.5,1],
    [ 1, 0.5,1],
    [-1, 0.5,1],
    [-1,-0.5,1]
])


# א. המלבן המקורי
rect_original = rectangle


# ב. סיבוב 30 מעלות
R30 = rotation_matrix(30)
rect_rotate30 = rectangle @ R30.T


# ג. סיבוב 45 ואז מתיחה פי 2 בציר x
R45 = rotation_matrix(45)
Sx = scale_x_matrix(2)

rect_rotate45_scale = rectangle @ R45.T
rect_rotate45_scale = rect_rotate45_scale @ Sx.T


# ד. מתיחה ואז סיבוב 45
rect_scale_rotate45 = rectangle @ Sx.T
rect_scale_rotate45 = rect_scale_rotate45 @ R45.T


# ציור כל המלבנים
plt.figure()

draw_rectangle(rect_original, "original")
draw_rectangle(rect_rotate30, "rotate 30")
draw_rectangle(rect_rotate45_scale, "rotate45 -> scaleX")
draw_rectangle(rect_scale_rotate45, "scaleX -> rotate45")

plt.axhline(0)
plt.axvline(0)

plt.legend()
plt.axis('equal')
plt.title("Rectangles Transformations")

plt.show()

print("Original rectangle:")
print(rect_original)