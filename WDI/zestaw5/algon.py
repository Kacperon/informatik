def trasa(N,tril,osil,a,b,trasy,osob):
    sumamin=10**10
    tablica_krok=[0 for _ in range(N)]
    for i in range(tril):
        tablica_krok[trasy[i][0]]+=1
        tablica_krok[trasy[i][1]]+=1
    print(tablica_krok)
    def reku(N,a,b,trasy,osob,poz1,poz2,suma,licznik,tablica_krok):
        nonlocal sumamin
        if poz2==b and suma<sumamin:
            sumamin=suma
        if licznik<N:
            for i in range(tablica_krok[licznik]):
                reku(N,a,b,trasy,osob,poz2,,suma,licznik,tablica_krok)


        




n=7
tril=8
osil=3
a=1
b=5
trasy=[[0,1,5],[1,2,21],[1,3,1],[2,4,7],[3,4,13],[3,5,16],[4,6,4],[5,6,1]]
osob=[0,2,3]
trasa(n,tril,osil,a,b,trasy,osob)