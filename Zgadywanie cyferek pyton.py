import random
print("Witaj w grze zgadywania liczby!")
a = int(input("Podaj liczbę:  "))   
x = random.randint(1, 100)
while a != x:
    if a < x:
        print("Twoja liczba jest mniejsza od wylosowanej liczby.")
    if a > x:
        print("Twoja liczba jest większa od wylosowanej liczby.")
    a = int(input("Spróbuj ponownie:  "))
    if a == x:
        print("Gratulacje! Zgadłeś liczbę.")





