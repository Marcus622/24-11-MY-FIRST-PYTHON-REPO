
# Aufgabe 1

Vorname = input("Wie ist dein Vorname? ")
Nachname= input("Wie ist dein Nachname? ")

print(f"Dein Name lautet: {Vorname} {Nachname}")

# Aufgabe 2

zahl1 = int(input("Gib die erste Zahl ein: "))
zahl2 = int(input("Gib die zweite Zahl ein: "))

print(f"Das Ergebnis beider Zahlen lautet: {zahl1+zahl2}")



# Aufgabe zur If-Bedingung

zahl3 = int(input("Gib eine beliebige Zahl ein: "))


if zahl3 >=0: # True --> Jump to the next line
    print("Die angegebene Zahl ist positiv") 

else:     
    print("Die angegebene Zahl ist negativ")

