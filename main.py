print("Calculate and transformation")


# Function to transform from RGB to CMYK
def c(r, g, b):
    w = max(r / 255, g / 255, b / 255)
    C = (w - r / 255) / w
    M = (w - g / 255) / w
    Y = (w - b / 255) / w
    K = 1 - w
    return C, M, Y, K


# main --------------------------------------------------------------

print()

print("The CMYK target values transformed from RGB output values are as follows:")

CMYK = c(75, 0, 130)

print()

print(str(CMYK))
