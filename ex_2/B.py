import numpy as np


# מטריצת הזזה
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

translation_matrix(5, 10)
