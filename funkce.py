from random import sample

def losuj(min=1, max=49, pocet=6):
    '''
    Funkce vytvoří sekvenci čísel od 'min' do 'max'.
    Vrací 'počet' náhodných čísel bez opakování v listu.
    '''
    sekvence = range(min, max + 1)
    return sample(sekvence, pocet)

def vsad_cisla(min=1, max=49, pocet=6):
    '''
    Funkce vybírá od uživatele 'pocet' čísel z intervalu
    'min' - 'max' bez opakování.
    Vrací list s vybranými čísly.
    '''
    cisla = []
    while len(cisla) < pocet:
        vstup = input("Zadej číslo: ")
        # test, jestli je zadaná hodnota číslo
        if not vstup.isnumeric():
            # pokud, ne upozorníme a skočíme do další iterace
            print(f"'{vstup}' není číslo!")
            continue
        # přetypovat na integer
        cislo = int(vstup)
        # pokud není ve správném intervalu, znovu
        if not max >= cislo >= min:
            print(f"'{cislo} není v intervalu {min}-{max}!")
            continue
        # pokud už máme, znovu
        if cislo in cisla:
            print(f"'{cislo} už mám!")
            continue
        # splněny všechny podmínky, ukládám
        cisla.append(cislo)

    return cisla