# This is a sample Python script.
import numpy as np
import matplotlib.pyplot as plt


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def f(x): return np.e**x


def integrate(func, a, b, nrects):
    """
    :param func: the function to integrate
    :param a: start of the integration; should be lower than b
    :param b: end of the integration; should be higher than a
    :param nrects: number of rectangles to sum
    :return: the value of the integrated function between a and b
    """
    dx = (b - a) / nrects
    lspace = np.linspace(a, b - dx, nrects)
    sum1 = 0

    for a in lspace:
        sum1 += func(a)

    return sum1 * dx


def integration_animation(func, a, b, nmax, speed):
    """
    :param func: the function to integrate
    :param a: start of integration
    :param b: end of integration
    :param nmax: stop after nmax rectangles
    :param speed: speed of the animation in seconds
    """
    dx = 0
    lspace1 = np.linspace(a, b, 1000)

    for i in range(nmax):

        plt.plot(lspace1, func(lspace1))
        dx = (b - a) / (i + 1)
        lspace = np.linspace(a , b - dx, i + 1)
        if i > 0:
            for t in lspace:
                if func(t) > 0:
                    plt.plot([t, t + dx], [0, 0], 'b')
                    plt.plot([t, t], [0, func(t)], 'b')
                    plt.plot([t + dx, t], [func(t), func(t)], 'b')
                    plt.plot([t + dx, t + dx], [func(t), 0], 'b')
                else:
                    if func(t) < 0:
                        plt.plot([t, t - dx], [0, 0], 'b')
                        plt.plot([t, t], [0, func(t)], 'b')
                        plt.plot([t - dx, t], [func(t), func(t)], 'b')
                        plt.plot([t - dx, t - dx], [func(t), 0], 'b')

        title = "n=" + str(i)
        plt.title(title)
        plt.show(block=False)
        plt.pause(speed)
        plt.clf()


if __name__ == '__main__':
    print(integrate(f, -3, 3, 50))
    integration_animation(f, -3, 3, 50, 0.1)
