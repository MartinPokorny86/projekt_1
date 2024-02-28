# 1. projekt: Textový analyzátor; na začátek přidat import sys
# u else nakonci dát sys.exit() pro ukončení programu

"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Martin Pokorny
email: pokornymartin2@gmail.com
discord: martin_pokorny86
"""
import sys

TEXTS = ['''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

usernames = ["bob", "ann", "mike", "liz"]
passwords = ["123", "pass123", "password123", "pass123"]

user = input("Zadej prihlasovaci jmeno:")
password = input("Zadej heslo:")

# nalezneme index přihlašovacího jména v seznamu usernames
index_user = usernames.index(user) if user in usernames else -1
# ověříme heslo a zapíšeme podmínku
verify_password = passwords[usernames.index(user)] if user in usernames else -1
# pokud ověření uživatele proběhlo v pořádku, pozdravíme uživatele
if index_user != -1 and verify_password == password:
  print("-" * 40)
  print(f"Ahoj {user}, zde je vyber textu k analyze:\n")
  # a dáme uživateli vybrat z možností dostupných textů
  for index, symbol in enumerate(TEXTS):
    print(f"ZNENI TEXTU CISLO {index + 1}:\n{symbol}\n")
  # ošetříme reakce kódu na různé možnosti vstupů od uživatele
  try:
    print("-" * 40)
    zadani_textu = input("Zadej cislo textu k analyze od 1 do 3: ")
    index_textu = int(zadani_textu) - 1
    # pokud uživatel zadá číslo, které není v zadání, program upozorní a skončí
    if index_textu not in range(0, 3):
      print("Cislo textu neni v zadani.")
      sys.exit()
    else:
      # počet slov
      slova_odstavec = TEXTS[index_textu].split("\n")
      for odstavec in slova_odstavec:
        new = odstavec.split(" ")
        vycisteno_1 = [abc_carka.strip(",, . ") for abc_carka in slova_odstavec]
      words = [word for text in vycisteno_1 for word in text.split()]
      print("-" * 40)

      print(words)
      print("Text cislo", zadani_textu, "obsahuje:", len(words), "slov.")
      # počet slov začínající velkým písmenem
      up_words = sum(1 for up_slovo in words if up_slovo.istitle())
      print(
          "Text cislo", zadani_textu, "obsahuje:", up_words,
          "slov začínajících velkým písmenem."
      )
      # počet slov psaných velkými písmeny
      upper_words = sum(
          1 for upper_slovo in words if upper_slovo.isalpha()
          and upper_slovo.isupper()
      )
      print(
          "Text cislo", zadani_textu, "obsahuje:", upper_words,
          "slov psaných velkými písmeny."
      )
      # počet slov psaných malými písmeny
      lower_words = sum(
          1 for lower_slovo in words if lower_slovo.islower()
      )
      print(
          "Text cislo", zadani_textu, "obsahuje:", lower_words,
          "slov psaných malými písmeny."
      )
      # počet čísel, ne cifer
      pocet_cisel = sum(
          1 for pocet_cisel in words if pocet_cisel.isdigit()
      )
      print(
          "Text cislo", zadani_textu, "obsahuje:", pocet_cisel,
          "cisel."
      )
      # suma všech čísel
      suma_cisel = sum(
          int(suma_cisel) for suma_cisel in words if suma_cisel.isdigit()
      )
      print(
          "Text cislo", zadani_textu, "ma soucet vsech cisel:", suma_cisel
      )
      # sloupcovy graf

      print(f"LEN: | OCCURENCES        | NR. ")

      pocty = {}
      for slovo in words:
        delka_slova = len(slovo)
        if delka_slova not in pocty:
          pocty[delka_slova] = 0
        pocty[delka_slova] += 1
      
      for delka, pocet in sorted(pocty.items()):
        if delka < 10:
          mezery = 17
          mezery_1 = 2
        else:
          mezery = 17
          mezery_1 = 1
        print(f"{delka} {' ' * mezery_1} | {'*' * pocet:<{mezery}} | {pocet}")

  # pokud uživatel vloží jiný datový typ vstupu než číslo, program upozorní a skončí se
  except ValueError:
    print("Zadal jsi jiny datovy typ nez cislo.")
    sys.exit()
# pokud uživatel není registrovaný, upozorníme jej a ukončíme program
else:
  print("Tvoje přihlašovací jméno nebo heslo nejsou v systému.")
  sys.exit()
