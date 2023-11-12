# Dane są dwie tablice mogące pomieścić taką samą liczbę elementów: T1[N][N] i T2[M], 
# gdzie M=N*N. W każdym wierszu tablicy T1 znajdują się uporządkowane rosnąco (w obrębie wiersza) liczby naturalne.
# Proszę napisać funkcję przepisującą wszystkie singletony (liczby występujące dokładnie raz) z tablicy T1 do T2,
# tak aby liczby w tablicy T2 były uporządkowane rosnąco. Pozostałe elementy tablicy T2 powinny zawierać zera.

def is_singleton(T1, num):
    n = len(T1)
    flag = False
    for i in range(n):
        for j in range(n):
            if T1[i][j] == num and not flag:
                flag = True
            elif T1[i][j] == num and flag:
                return False
    
    return True

def push(T2, num, i): # wpychanie w danej tablicy liczby na dane miejsce i przesuwanie reszty
    n = len(T2)
    tmp = T2[i]
    T2[i] = num
    for j in range(i + 1, n):
        tmp, T2[j] = T2[j], tmp # podstawianie w petli
        if T2[j] == 0:
            break

def pseudosort(T2, num): # ma znalezc pozycje gdzie wepchnac liczbe
    n = len(T2)
    i = 0

    while T2[i] < num:
        if T2[i] == 0:
            T2[i] = num
            return
        i += 1
    if i == n - 1: # bo na koncu i tak nie ma szans, ze wywalimy jakas wartosc z tablicy
        T2[i] = num
        return
    else:
        push(T2, num, i)

def zad6(T1): # czy liczba z tablicy to singleton, jak tak to gdzie ja wstawic i wstawic oraz posortowac
    n = len(T1)
    T2 = [0 for _ in range(n * n)]

    for i in range(n):
        for j in range(n):
            if is_singleton(T1, T1[i][j]): 
                pseudosort(T2, T1[i][j])

    return T2

T1 = [[12, 7, 5], [5, 8, 6], [7, 9, 1]]
print(zad6(T1))