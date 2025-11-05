from matplotlib import pyplot as plt

def plot_polynomial(a, b, c, xs):
    ys = [y(a, b, c, x) for x in xs]

    plt.plot(xs, ys)
    plt.title(f'f(x) ={coeff_string(a)}x^2{coeff_string(b)}x{coeff_string(c)}')
    plt.xlabel("x")
    plt.ylabel("f(x)")

def y(a, b, c, x):
    return a*x**2 + b * x + c

def coeff_string(coefficient):
    if coefficient == 1:
        return " + "
    elif coefficient == 0:
        return None
    elif coefficient >= 0:
        return f" + {coefficient}"
    elif coefficient < 0:
        return f" - {abs(coefficient)}"

if __name__ == "__main__":
    plot_polynomial(1, -5, 100, [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10])
    plt.show()