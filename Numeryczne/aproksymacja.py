import numpy as np
import matplotlib.pyplot as plt

def wczytaj_dane_z_pliku(nazwa_pliku):
    dane = np.loadtxt(nazwa_pliku)
    x = dane[:, 0]
    y = dane[:, 1]
    return x, y

def aproksymacja_wielomianowa(x, y, stopien):
    wspolczynniki = np.polyfit(x, y, stopien)
    wielomian = np.poly1d(wspolczynniki)
    return wielomian

def wypisz_wzor(wielomian):
    print("\nFunkcja aproksymacyjna:")
    print(wielomian)

def rysuj_punkty(x, y):
    plt.scatter(x, y, color='red', label='Dane wejściowe')
    plt.title('Punkty z pliku')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()

def rysuj_wykres_aproksymacji(x, y, wielomian, stopien):
    x_gest = np.linspace(min(x), max(x), 500)
    y_apr = wielomian(x_gest)

    plt.scatter(x, y, color='red', label='Dane wejściowe')
    plt.plot(x_gest, y_apr, color='blue', label=f'Aproksymacja {stopien}-go stopnia')
    plt.title(f'Aproksymacja wielomianowa stopnia {stopien}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    nazwa_pliku = input("Podaj nazwę pliku z danymi (np. dane.txt, dane1.txt): ")
    try:
        x, y = wczytaj_dane_z_pliku(nazwa_pliku)
    except Exception as e:
        print(f"Błąd podczas wczytywania danych: {e}")
        return

    # Pokaż punkty
    rysuj_punkty(x, y)

    # Zapytaj o stopień
    stopien = int(input("Podaj stopień aproksymacji (1, 2 lub 3): "))
    if stopien not in [1, 2, 3]:
        print("Nieprawidłowy stopień. Dozwolone: 1, 2 lub 3.")
        return

    # Aproksymacja i rysunek
    wielomian = aproksymacja_wielomianowa(x, y, stopien)
    wypisz_wzor(wielomian)
    rysuj_wykres_aproksymacji(x, y, wielomian, stopien)

if __name__ == '__main__':
    main()
