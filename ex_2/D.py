import numpy as np


def translation_matrix(a, b):

    T = np.array([
        [1, 0, a],
        [0, 1, b],
        [0, 0, 1]
    ])

    print("Translation matrix (a =", a, ", b =", b, "):")
    print(T)
    print()

    return T


def rotation_matrix(theta):

    theta_rad = np.radians(theta)

    R = np.array([
        [np.cos(theta_rad), -np.sin(theta_rad), 0],
        [np.sin(theta_rad),  np.cos(theta_rad), 0],
        [0, 0, 1]
    ])

    print("Rotation matrix (theta =", theta, "degrees):")
    print(R)
    print()

    return R



def rotate_around_point():

    T1 = translation_matrix(-100, -200)
    R = rotation_matrix(30)
    T2 = translation_matrix(100, 200)

    M = T2 @ R @ T1

    print("Rotation of 30 degrees around point (100,200):")
    print(M)
    print()

    return M

rotate_around_point()