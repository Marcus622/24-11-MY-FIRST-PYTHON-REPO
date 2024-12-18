# Zeitverschiebung berechnen:
# Implementiere eine Funktion zeit_in_zukunft(), die eine Eingabe von Minuten, Stunden oder Tagen vom Benutzer 
# entgegennimmt und das Datum und die Uhrzeit berechnet, die nach dieser Zeitspanne liegt.
# Beispiel: Wenn der Benutzer 2 Stunden eingibt und die aktuelle Zeit 14:00 ist, sollte das Programm 16:00 ausgeben.

from datetime import datetime, timedelta

def zeit_in_zukunft():
    aktuelle_zeit = datetime.now()

    print('Gib die gewünschte Zeitspanne ein: ')
    zeitspanne = input("Gib eine Zahl, gefolgt von Minuten, Stunden, oder Tagen ein:")
    try:
        anzahl, einheit = zeitspanne.split()
        anzahl = int(anzahl)

        if einheit.lower() == "minuten":
            zukunft = aktuelle_zeit + timedelta(minutes=anzahl)
        elif einheit.lower() == "stunden":
            zukunft = aktuelle_zeit + timedelta(hours=anzahl)
        elif einheit.lower() == "tagen":
            zukunft = aktuelle_zeit + timedelta(days=anzahl)
        else:
            print("Ungültige Eingabe. Gib Minuten, Stunden, oder Tagen ein")
            return

        print(f"Die Zeit nach {anzahl} {einheit} wird: {zukunft.strftime('%Y-%m-%d %H:%M:%S')}")

    except ValueError:
        print("Ungültige Eingabe. Bitte gib eine Zahl gefolgt von der Einheit (Minuten, Stunden oder Tagen) ein.")

zeit_in_zukunft()