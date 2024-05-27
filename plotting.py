from matplotlib import pyplot as plt


def draw_plot(a, b, func, name, dx=0.001):
    xs, ys = [], []
    a -= dx
    b += dx
    x = a
    while x <= b:
        xs.append(x)
        ys.append(func(x))
        x += dx
    plt.plot(xs, ys, 'g', label=name)


def plot(name, xs, ys, P, x):
    plt.title(name)
    draw_plot(xs[0], xs[-1], P, name)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.scatter(x, P(x), c='r')
    for i in range(len(xs)):
        plt.scatter(xs[i], ys[i], c='b')

    plt.show()
