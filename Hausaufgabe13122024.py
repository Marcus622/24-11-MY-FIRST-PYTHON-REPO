# Die Ferien sind in Reichweite

date_today = input("Welcher Tag ist heute (JJJJ.MM.TT)?")
# Winterferien 2024 2024.12.24-2025.01.01
# Ostern 2025.04.18-2025.04.21
# Sommerferien 2025.08.11-2025.08.19
# 1.Mai 2025.05.01
# Christi Himmelsfahrt 2025.05.29
# Pfingstmontag 2025.06.09
# Tag der deutschen Einheit 2025.10.03
# Reformationstag 2025.10.31
# Winterferien 2025 225.12.24-2026.01.01

WinterHolidaysStart24 = "2024.12.23"
WinterHolidaysEnd24 = "2025.01.02"
EasterHolidaysStart25 = "2025.04.17"
EasterHolidaysEnd25 = "2025.04.22"
SummerHolidaysStart25 = "2025.08.08"
SummerHolidaysEnd25 = "2025.08.20"
WinterHolidaysStart25 = "2025.12.23"
WinterHolidaysEnd25 = "2026.02.01"
first_may = "2025.05.01"
christi_verpissimus = "2025.05.29"
pfimo = "2025.06.09"
day_of_dawn = "2025.10.03"
martin_luther_day = "2025.10.31"

if  WinterHolidaysStart24 <= date_today <= WinterHolidaysEnd24:
    print("Du hast frei.")
elif EasterHolidaysStart25 <= date_today <= EasterHolidaysEnd25:
    print("Du hast frei.")
elif SummerHolidaysStart25 <= date_today <= SummerHolidaysEnd25:
    print("Du hast frei.")
elif WinterHolidaysStart25 <= date_today <= WinterHolidaysEnd25:
    print("Du hast frei.")
elif date_today == first_may:
    print("Du hast frei.")
elif date_today == christi_verpissimus:
    print("Du hast frei.")
elif date_today == pfimo:
    print("Du hast frei.")
elif date_today == day_of_dawn:
    print("Du hast frei.")
elif date_today == martin_luther_day:
    print("Du hast frei.")

else:
    print("Leider verloren, sofern es kein Wochenende ist. Die Pflicht ruft.")