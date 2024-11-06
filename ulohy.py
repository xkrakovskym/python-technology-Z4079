# 1. Napíšte skript, ktorý importuje modul math a vypočíta druhú odmocninu zo 64.
# Výsledok vytlačte na obrazovku. Použite funkciu sqrt. Vypíšte aj výsledok.

import math
#print(math.sqrt(64))

# 2. Z modulu random importujte iba funkciu randint a použite ju na vygenerovanie
# náhodného celého čísla medzi 1 a 10. Výsledok vytlačte.

from random import randint

#print(randint(1,10))

# 3. Importujte modul datetime ako dt a použite ho na vytlačenie aktuálneho dátumu a času.
# Použite funkciu datetime.now()

#import datetime as dt

#print(dt.datetime.now())

# 4. . Inštalácia balíka:
# Napíšte príkaz pip, ktorý nainštaluje balík requests.
# Po inštalácii balíka requests napíšte skript, ktorý ho importuje a pošle GET
# požiadavku na https://google.com. Vytlačte status kód odpovede.

import requests

response = requests.get("https://google.com")