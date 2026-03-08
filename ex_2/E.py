import numpy as np

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
rotation_matrix(30)


