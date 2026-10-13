import random

print("Witaj w grze zgadywania liczby!")
x = random.randint(1, 100)  # Komputer losuje raz na początku
b = 0  # Licznik prób

while True:
  wejscie = input("Podaj liczbę: ")

  # Sprawdzamy, czy użytkownik wpisał cyfry
  if wejscie.isdigit():
    a = int(wejscie)
    b += 1  # Zwiększamy licznik prób przy każdym wpisaniu
  else:
    print("To nie jest liczba. Spróbuj ponownie.")
    continue  # Wraca do początku pętli i pyta ponownie

  # Sprawdzamy warunki gry
  if a < x:
    print("Twoja liczba jest mniejsza od wylosowanej.")
    print("Liczba prób: ", b)
  elif a > x:
    print("Twoja liczba jest większa od wylosowanej.")
    print("Liczba prób: ", b)
  else:
    print("Gratulacje! Zgadłeś liczbę.")
    print("Liczba prób: ", b)
    break  # Przerywamy pętlę, bo gra skończona!


