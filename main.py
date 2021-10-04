# Ciag Collatza:
# Wejscie: z klawiatury liczba X z zakresu [1 - 100].
# Kolejny element ciagu:
#       - jesli X parzyste to X/2
#       - jesli X nieparzyste to 3*X + 1
# Ostatni element ciagu: 1.
# Wyjscie: liczba elementow ciagu.
# Pomijam obsluge bledow wprowadzania, wprowadzane moga byc liczby naturalne.

print('---------------------------------------------------------------')
print('Ciag Collatza')
print('Podaj X - liczbe naturalna z zakresu [1, 100]: ', end='')
pierwszy_wyraz_ciagu = int(input())
wyraz_ciagu = pierwszy_wyraz_ciagu
licznik = 1

while wyraz_ciagu > 1:
  if wyraz_ciagu % 2 == 0:
    wyraz_ciagu = wyraz_ciagu / 2
  else:
    wyraz_ciagu = 3 * wyraz_ciagu + 1

  licznik += 1

print('Liczba wyrazow ciagu Collatza dla X = {} to: {}'
      .format(pierwszy_wyraz_ciagu, licznik))
