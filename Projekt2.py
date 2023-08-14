"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

Druhý projekt je hra Bull & Cows 
Hra je na principu hádání 4 ciferného tajného unikátního čísla
které ma za úkol hráč uhodnout, číslo nesmí začínat 0 musí mít 4 čísla, 
nesmí obsahovat písmena a duplicitní znaky. Program vygeneruje číslo, poté hráč
háda vždy č mísné číslo, jestliže uhodne číslo a správné pořadí 
vždy se mu přičte 1 bull jestliže uhodne jen číslo přičítá se cow.
Hra konnčí uhodnutím čísla ve správném pořadí. 

author: Zdeněk Fojt
email: zdenek.fojt@gmail.com
discord: Zdeněk F.
"""
# Naimportuj nahodna cisla
import random

oddelovac = "-" * 50

# Uvitej uzivatele u hry 
print("Ahoj, vítej u hry!")
print(oddelovac)

print(
    f"Vygeneroval jsem pro tebe 4místné náhodné číslo",
    f"Pojď, si zahrát hru Bulls and cows", sep="\n"    
    )
print(oddelovac)


# Vygeneruj 4 mistne tajne_cislo:
    # tajne cislo nesmi zacinat 0:
def vygeneruj_nahodne_cislo():
    while True:
        tajne_cislo = ''.join(random.sample('123456789', 4))
        if tajne_cislo[0] != '0':
            return tajne_cislo
    
# Hadej cislo:
    # kdyz bude spravne cislo na spravne pozici:
        #bulls +1
    # kdyz bude jen spravne cislo:
        #cows +1     
def hadej_cislo(tajne_cislo,odhad):
    
    bulls, cows = 0, 0
    for cislice in range(len(tajne_cislo)):
        if odhad[cislice] == tajne_cislo[cislice]:
            bulls += 1
        elif odhad[cislice] in tajne_cislo:
            cows += 1
    return bulls, cows

# Zkontroluj cislo jestli ma spravny tvar:
    # Kontrola délky čísla:
    # Kontrola duplicity
    # Kontrola začínání nulou
    # Kontrola, zda všechny znaky jsou číslice
def zkontroluj_cislo(odhad):
    if len(odhad) != 4:
        return False
    
    if len(set(odhad)) != 4:
        return False
    
    if odhad[0] == "0":
        return False
    
    if not odhad.isdigit():
        return False

    return True
   
#Uprav vystup bulls, cows s ohledem na jednotne a mnozne cislo
def uprav_vystup(tajne_cislo, odhad):
    bulls = sum(1 for cislice in range(4) if odhad[cislice] == tajne_cislo[cislice])
    cows = sum(1 for cifra in odhad if cifra in tajne_cislo) - bulls

    bulls_str = "bull" if bulls == 1 else "bulls"
    cows_str = "cow" if cows == 1 else "cows"

    return f"{bulls} {bulls_str}, {cows} {cows_str}"

def main():
    tajne_cislo = vygeneruj_nahodne_cislo()
    pokusy = 0
   
    while True:
        odhad = input("Hádej číslo:")
        if not zkontroluj_cislo(odhad):
            print(f"Špatné číslo",
                  f"{oddelovac}", sep="\n")
            continue
        
        pokusy += 1
        vystup = uprav_vystup(tajne_cislo, odhad)
      
        if vystup == "4 bulls, 0 cows":
            print("Gratluji, VÝHRA JE TVOJE!")
            break
        else:
            print(
                f"{vystup}",            
                f"{oddelovac}", sep="\n"
                )

            
if __name__ == "__main__":
    main()

