# FKF_ertesito
FKF oldalán ellenőrzi a szemétszállítási periódust és értesíti a felhasználót annak közeledtéről. 
Fontos!
Létrehoz egy Task-ot(FKF értesítő néven) a Feladatütemezőben(Windows) és minden nap 10:00-kor lekéri az adatokat, majd értesíi a fehasználót.
Be kell állítani kézzel hogy a legmagasabb futtatási privilégiummal fusson, különben nem tud logolni és ezért nem fut le a program(fejlesztés alatt)


Config.txt-ben tárolt adatok alapján működik a lekérdezés:
1. QueryPeriod(fejlesztés alatt):
2. District: Kerület száma pl.: 1111
3. Public Place: Utcanév pl.: Aranyos---utca
4. HouseNumber: házszám pl.: 34

Első alkalommal generál egy konfig fájl-t és konzolon bekéri a megfelelő adatokat a felhasználótól, majd elmenti egy fájlba a FKF_lekerdezes.py mellé. Miután bekonfiguráltuk már nem kéri ezeket az adatokat., ha módosítani szeretnénk az adatokon a jelenlegi állapotában, akkor töröljük a Config.txt-t és generáltassunk egy újat.
