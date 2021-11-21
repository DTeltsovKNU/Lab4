#aaaaaa

import numpy as np
import matplotlib.pyplot as plt

def der(x,y,z):
    return round(np.cos(x) * z - np.sin(x) * y + np.sin(x),4)


def euler(a,b,c,h):
    x = a
    y = b
    z = c
    x_l = [x]
    y_l = [y]
    z_l = [z]
    print('X_1: {0}   Y_1: {1}   Z_1 {2}'.format(x,y,z))
    for i in range(9):
        z = round(z + (der(x,y,z) * h), 4)
        x = round(x+h,4)
        y = round(y + h*z,4)
        x_l.append(x)
        y_l.append(y)
        z_l.append(z)
        print('X_{2}: {0}   Y_{2}: {1}   Z_{2}: {3}   Der_{2}: {4}'.format(x,y,i+2,z, der(x,y,z)))
    return y_l,x_l




def main():
    z = 0
    goal = 2
    eps = 0.01
    y_l,x_l = euler(round(-np.pi,4), 2, z, 0.6981)
    while True:
        if np.abs(y_l[9] - goal) < eps:
            break
        if y_l[9] > goal:
            z = round(z - eps, 4)
        else:
            z = round(z + eps,4)
        y_l,x_l = euler(round(-np.pi,4), 2, z, 0.6981)
    print(z)
    plt.plot(x_l, y_l)
    plt.show()


if __name__ == '__main__':
    main()