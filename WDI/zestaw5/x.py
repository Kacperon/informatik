def rozwiaz_sudoku():
    sudoku = [
        [7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]
    ]

    def rozwiaz(T):
        puste = do_uzupelnienia(T)

        if not puste:                       # jeśli nie ma pustych miejsc w sudoku- zwróć True
            return True
        else:
            w, k = puste

        for i in range(1,10):
            if sprawdz(T, i, (w, k)):       # sprawdz, czy liczbę i można wstawić na to miejsce
                T[w][k] = i                 # wstaw liczbę i
                if rozwiaz(T): return True  # jeśli uda się rozwiązać tym podstawieniem- jupii
                T[w][k] = 0                 # jeśli się nie uda- próbujemy podstawić inną liczbę
        return False

    def sprawdz(T, liczba, pozycja):
        for i in range(len(T[0])):
            if T[pozycja[0]][i] == liczba and pozycja[1] != i:  # jeżeli w danym rzędzie jest liczba którą chcemy wstawić, w kolumnie
                return False                                    # różnej od tej, gdzie chcemy wstawić, zwróć False

        for i in range(len(T)):
            if T[i][pozycja[1]] == liczba and pozycja[0] != i:  # jeżeli w danej kolumnie jest liczba, którą chcemy wstawić, w wierszu
                return False                                    # różnym od tego, gdzie chcemy wstawić- False

        w_kwadrat = pozycja[0] // 3
        k_kwadrat = pozycja[1] // 3

        for i in range(w_kwadrat*3, w_kwadrat*3 + 3):
            for j in range(k_kwadrat * 3, k_kwadrat*3 + 3):
                if T[i][j] == liczba and (i,j) != pozycja:      # jeżeli w kwadracie jest już liczba, którą chcemy wstawić, na pozycji
                    return False                                # różnej od tej, na którą chcemy wstawić- False

        return True

    def do_uzupelnienia(T):                 # znajduje pierwsze następne puste miejsce
        for i in range(len(T)):
            for j in range(len(T[0])):
                if T[i][j] == 0:
                    return i, j
        return None                         # jeśli nie ma pustych miejsc- zwróć None

    rozwiaz(sudoku)
    for i in sudoku:
        print(i)

def problem_8_hetmanow():
    def mozliwe(T, zakw, zakk, zakprz1, zakprz2):
        moz = []
        for i in range(8):
            for j in range(8):
                if T[i][j] == 0 and i not in zakw and j not in zakk and i-j not in zakprz1 and j+i not in zakprz2:
                    moz += [(i,j)]
        if len(moz) == 0:
            return None
        return moz

    def rozwiaz(T, zakw=[], zakk=[], zakprz1=[], zakprz2=[], n = 0):
        wolne = mozliwe(T, zakw, zakk, zakprz1, zakprz2)
        if not wolne:
            if n == 8:
                for i in T:
                    print(i)
                return True
            return False
        else:
            for i in wolne:
                w,k = i
                T[w][k] = 1
                if rozwiaz(T, zakw+[w], zakk+[k], zakprz1+[w-k]+[abs(w-k)], zakprz2+[k+w], n+1): return True
                T[w][k] = 0

    T = [[0 for _ in range(8)] for _ in range(8)]
    rozwiaz(T)