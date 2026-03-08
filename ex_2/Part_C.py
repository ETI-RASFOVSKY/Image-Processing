# Interpolation functions

def nearest_neighbor(alpha, beta, I00, I01, I10, I11):

    if alpha < 0.5 and beta < 0.5:
        value = I00
    elif alpha >= 0.5 and beta < 0.5:
        value = I01
    elif alpha < 0.5 and beta >= 0.5:
        value = I10
    else:
        value = I11

    print("Nearest Neighbor Result:")
    print(value)
    print()

    return value


def bilinear_interpolation(alpha, beta, I00, I01, I10, I11):

    value = (
        (1 - alpha) * (1 - beta) * I00 +
        alpha * (1 - beta) * I01 +
        (1 - alpha) * beta * I10 +
        alpha * beta * I11
    )

    print("Bilinear Interpolation Result:")
    print(value)
    print()

    return value


# Example run
alpha = 0.3
beta = 0.6

I00 = 10
I01 = 20
I10 = 30
I11 = 40

nearest_neighbor(alpha, beta, I00, I01, I10, I11)

bilinear_interpolation(alpha, beta, I00, I01, I10, I11)