import random
b = 0
print("Witaj w grze zgadywania liczby!")
a = int(input("Podaj liczbę:  "))   
x = random.randint(1, 100)
while a != x:
    if a < x:
        print("Twoja liczba jest mniejsza od wylosowanej liczby.") 
        b += 1
        print("Liczba prób: ", b)
    if a > x:
        print("Twoja liczba jest większa od wylosowanej liczby.")
        b += 1
        print("Liczba prób: ", b)
    a = int(input("Spróbuj ponownie:  "))
    if a == x:
        print("Gratulacje! Zgadłeś liczbę.")
        print ("Liczba prób: ", b)





