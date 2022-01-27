import numpy as np 


## Use numpy.power
def derivative(z):
    f = np.multiply(z, z)
    g = np.multiply(z, f)
    der = 4 * g
    return der

def poly(z):
    f = np.multiply(z, z)
    g = np.multiply(f, f)
    h = g - 1
    return h

def newton(z):
    z_next = z - poly(z)/derivative(z)
    return z_next


if __name__ == '__main__':

    xmin = 0
    xmax = 5
    xn = 6
    ymin = 0
    ymax = 5
    yn = 6


    X = np.linspace(xmin, xmax, xn).astype(np.float32)
    Y = np.linspace(ymin, ymax, yn).astype(np.float32)

    C = X + Y[:, None] * 1j

    isConvergent = np.zeros_like(C, dtype = bool)
    values = np.zeros_like(C, dtype = int)
    values_next = np.zeros_like(C, dtype = int)


    stillChecking = np.ones_like(C, dtype = bool)

    values_next = np.array(C)

    values_next[stillChecking] = newton(values_next[stillChecking])

