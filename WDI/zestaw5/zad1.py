def czy_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def wykresl_jedna_cyfre_i_sprawdz_pierwsze_rekurencyjnie(liczba, potega_10):
    if potega_10 == 0:
        return

    nowa_liczba = liczba // potega_10 // 10 * potega_10 + liczba % potega_10

    if nowa_liczba >= 10 and czy_pierwsza(nowa_liczba):
        print(nowa_liczba)

    wykresl_jedna_cyfre_i_sprawdz_pierwsze_rekurencyjnie(liczba, potega_10 // 10)
    wykresl_jedna_cyfre_i_sprawdz_pierwsze_rekurencyjnie(nowa_liczba, potega_10 // 10)

# Przykład użycia
liczba_wejsciowa = int(input("Podaj liczbę całkowitą: "))
potega_10 = 10 ** (len(str(liczba_wejsciowa)) - 1)
wykresl_jedna_cyfre_i_sprawdz_pierwsze_rekurencyjnie(liczba_wejsciowa, potega_10)