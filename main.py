import random
import math

# Zadatak 1 - Kreiranje liste proizvoda
proizvodi = ["Laptop", "Miš", "Tastatura", "Monitor", "Slušalice", "USB kabl", "Punjač", "Tablet"]

# Zadatak 2 - Kreiranje rečnika sa cenama
cene = {
    "Laptop": 950.99,
    "Miš": 19.99,
    "Tastatura": 49.99,
    "Monitor": 379.99,
    "Slušalice": 79.99,
    "USB kabl": 9.99,
    "Punjač": 24.99,
    "Tablet": 429.99
}

# Zadatak 3 - Prikaz svih proizvoda i cena
print("Svi proizvodi i cene:")
for proizvod in proizvodi:
    print(f"{proizvod} - {cene[proizvod]} €")

# Zadatak 4 - Unos budžeta i filtriranje
print()
budzet = float(input("Unesite svoj budžet u evrima: "))
print(f"Proizvodi koje možete da priuštite sa budžetom od {budzet} €:")
for proizvod in proizvodi:
    if cene[proizvod] <= budzet:
        print(f"  {proizvod} - {cene[proizvod]} €")

# Zadatak 5 - Funkcija najskuplji_proizvod()
def najskuplji_proizvod():
    return max(cene, key=cene.get)

print()
najskuplji = najskuplji_proizvod()
print(f"Najskuplji proizvod je: {najskuplji} - {cene[najskuplji]} €")

# Zadatak 6 - Korišćenje random modula
print()
nasumican_proizvod = random.choice(proizvodi)
print(f"Korisniku je privukao pažnju proizvod: {nasumican_proizvod}")

# Zadatak 7 - Korišćenje math modula
print()
zbir_cena = math.fsum(cene.values())
prosecna_cena = round(zbir_cena / len(cene), 2)
print(f"Prosečna cena svih proizvoda je: {prosecna_cena} €")

# Zadatak 8 - Broj prodatih komada i ukupan prihod
prodati_komadi = [15, 120, 85, 30, 60, 200, 95, 25]

ukupan_prihod = 0
for i in range(len(proizvodi)):
    ukupan_prihod += cene[proizvodi[i]] * prodati_komadi[i]

print()
print(f"Ukupan prihod: {round(ukupan_prihod, 2)} €")

# Zadatak 9 - Dodavanje novog proizvoda
novi_proizvod = "Zvučnik"
nova_cena = 59.99

proizvodi.append(novi_proizvod)
cene[novi_proizvod] = nova_cena

print()
print("Ažurirana lista proizvoda:")
for proizvod in proizvodi:
    print(f"  {proizvod} - {cene[proizvod]} €")

# Zadatak 10 - Sortiranje proizvoda po ceni
sortirani_proizvodi = sorted(proizvodi, key=lambda p: cene[p])

print()
print("Proizvodi sortirani po ceni (od najjeftinijeg ka najskupljem):")
for proizvod in sortirani_proizvodi:
    print(f"{proizvod} - {cene[proizvod]} €")
