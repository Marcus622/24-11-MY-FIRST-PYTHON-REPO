# Wochentag berechnen:
#Erstelle eine Funktion wochentag_berechnen(), die den Wochentag für ein beliebiges eingegebenes Datum berechnet und 
# ausgibt (z. B. Montag, Dienstag usw.).

from datetime import datetime
def wochentag_berechnen():
    while True:
        benutzereingabe = input("Gib ein Datum im Format JJJJ.MM.TT ein: ")

        try:
            eingegebenes_datum = datetime.strptime(benutzereingabe, "%Y.%m.%d")

            wochentage = ["Montag, Dienstag, Mittwoch, Donnerstag, Freitag, Samstag, Sonntag"]
            wochentag = wochentage[eingegebenes_datum.weekday()]

            print(f"Der Wochentag für das Datum {benutzereingabe} ist: {wochentag}.")
            break
        except ValueError

wochentag_berechnen()