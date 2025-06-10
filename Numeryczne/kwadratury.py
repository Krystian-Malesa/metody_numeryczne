import numpy as np
import matplotlib.pyplot as plt

def fun_kwadratowa(x, a, b, c):
    # f(x) = a x² + b x + c
    return a*x**2 + b*x + c

def obliczanie_trapezowe(x, y):
    # odstęp między punktami
    krok  = x[1] - x[0]
    
    # pierwszy i ostatni wyraz
    y_start = y[0]
    y_end   = y[-1]
    
    # suma wartości środkowych (bez pierwszego i ostatniego)
    middle_values = y[1:-1]
    sum_middle = 0
    for val in middle_values:
        sum_middle += val
    
    double_middle = 2 * sum_middle # double middle ∑ n−1 i=1
    
    # całościowa suma wagowana
    total = y_start + double_middle + y_end
    
    # wynik całki trapezami
    result = krok  * total / 2
    return result


def obliczanie_prostokątne(x, y):
    krok = x[1] - x[0]
    
    # od lewej
    left_heights = y[:-1]
    total_height = 0
    for h in left_heights:
        total_height += h
    
    area = krok * total_height
    return area

def plot_approx(x, y, method='trapezy'):
    # trapezy
    if method == 'trapezy':
        for i in range(len(x)-1):
            xs = [x[i], x[i], x[i+1], x[i+1]]
            ys = [0, y[i], y[i+1], 0]
            plt.fill(xs, ys, facecolor='orange', edgecolor='k', alpha=0.4)
    else:  # 'prostokąty'
        for i in range(len(x)-1):
            xs = [x[i], x[i], x[i+1], x[i+1]]
            ys = [0, y[i], y[i], 0]
            plt.fill(xs, ys, facecolor='blue', edgecolor='k', alpha=0.4)

def main():
    # wejście od użytkownika
    a, b, c = map(int, input("Podaj a, b, c: ").split())
    x0, x1 = map(int, input("Zakres [x0 x1]: ").split())
    n_trap = int(input("Liczba przedziałów (trapezy): "))
    n_rect = int(input("Liczba przedziałów (prostokąty): "))

    # wektory x i y
    xs_trap = np.linspace(x0, x1, n_trap+1)
    ys_trap = fun_kwadratowa(xs_trap, a, b, c)
    xs_rect = np.linspace(x0, x1, n_rect+1)
    ys_rect = fun_kwadratowa(xs_rect, a, b, c)

    # obliczenia
    I_trap = obliczanie_trapezowe(xs_trap, ys_trap)
    I_rect = obliczanie_prostokątne(xs_rect, ys_rect)

    print(f"Metoda trapezów = {I_trap}")
    print(f"Metoda prostokątów = {I_rect}")

    # wykres funkcji
    x_plot = np.linspace(x0, x1, 200)
    y_plot = fun_kwadratowa(x_plot, a, b, c)
    plt.plot(x_plot, y_plot, 'b-', lw=2)

    # nakładanie przybliżeń
    plot_approx(xs_trap, ys_trap, method='trapezy')
    plt.show()

    plt.plot(x_plot, y_plot, 'b-', lw=2)
    plot_approx(xs_rect, ys_rect, method='rect')
    plt.show()

if __name__ == '__main__':
    main()
