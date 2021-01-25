from mpmath import mp
mp.dps = 50 # dokładność
print(mp.quad(lambda x: (mp.cos(x) - mp.exp(x))*mp.csc(x), [-0.9999999999999999, 1]))
#Zakres nie zaczyna się od -1 ponieważ wartość funkcji w tym punkcie jest bardzo bliska 0 i program sie wypisuje
#Natomiast zastępując liczbe -1 bardzo bliską -1 otrzymujemy wynik bardzo poprawny z dokładnościa większa niz 10 cyfr
