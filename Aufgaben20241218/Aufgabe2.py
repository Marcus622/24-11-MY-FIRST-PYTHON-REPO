#2. Differenz bis zum Jahresende berechnen:
# Schreibe eine Funktion tage_bis_jahresende(), die die Anzahl der 
# Tage vom aktuellen Datum bis zum 31. Dezember des aktuellen Jahres 
# berechnet.
# Hinweis: Verwende datetime.date oder datetime.datetime zur Berechnung

import datetime

def tage_bis_jahresende():
    heute = datetime.date.today()

    jahresende = datetime.date(2024,12,31)
    differenz = jahresende - heute
    return differenz.days

print("Es sind noch "+str(tage_bis_jahresende())+" Tage bis Jahresende.")
