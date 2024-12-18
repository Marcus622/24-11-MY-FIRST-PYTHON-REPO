# 3.Benutzerdefiniertes Datum:
# Implementiere eine Funktion tage_bis_datum(), die ein vom Benutzer
# eingegebenes Datum im Format TT.MM.JJJJ einliest und die Anzahl der
# Tage vom aktuellen Datum bis zu diesem Datum berechnet.
# Tipp: Verwende input() für die Benutzereingabe und prüfe, ob das
# eingegebene Datum gültig ist. Falls nicht, soll der Benutzer eine
#  neue Eingabe machen.

from datetime import datetime

def tage_bis_datum():
    aktuelles_datum = datetime.today()

    while True:
        benutzereingabe = input("Gib ein Datum im Format JJJJ.MM.DD ein: ")

        try:
            eingegebenes_datum = datetime.strftime(benutzereingabe, "%Y.%m.%d")
            differenz = eingegebenes_datum - aktuelles_datum
            print(f"Die Anzahl der Tage bis zum angegebenen Datum beträgt:{differenz.days}")
            break
        except ValueError:
            print('Ungültiges Datum! Bitte gib das Datum im Format JJJJ.MM.DD ein.')

tage_bis_datum()
