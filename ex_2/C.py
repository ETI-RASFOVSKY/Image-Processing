import numpy as np

def scale_matrix(sx, sy=None):

    if sy is None:
        sy = sx

    S = np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])

    print("Scale matrix (sx =", sx, ", sy =", sy, "):")
    print(S)
    print()

    return S
scale_matrix(2, 3)