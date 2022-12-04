import random
import time
import pandas as pd

woordfile = pd.read_excel (r'C:\Users\swede\Documents\Persoonlijk\Python\twaalfletterwoorden.xlsx', engine='openpyxl')
woordenlijst = list(woordfile.iloc[:,0])

def randomwoordpick():
    woord = ''
    while len(woord) != 12:
        woord = random.choice(woordenlijst)
    return woord

    
        
def hussel(woord):
    hussel = ''
    while woord:
        positie = random.randrange(len(woord))
        hussel += woord[positie]
        woord = woord[:positie] + woord[(positie+1):]
    return hussel

def layout(hussel): #woord volgens juiste format geprint boven cijferrij
    HUSSEL = hussel.upper()
    woordhoop = ''
    for i in range(12):
        woordhoop += HUSSEL[i]+'  '
    woordhoop = woordhoop[:-2]
    print(woordhoop)
    cijferhoop = ''
    for i in range(1,10):
        cijferhoop += str(i)+'  '
    for i in range(10,13):
        cijferhoop += str(i)+' '
    cijferhoop = cijferhoop[:-1]
    print(cijferhoop)

def letterverander(woord,l,i): #woord in een lijst gezet om individ letter aan te passen
    nwoord = ''
    woordlijst = list(woord)
    woordlijst[i]= l
    for letter in woordlijst:
        nwoord += letter
    return nwoord


    
def raden(hussel,antwoord, correct, naam):
    l = 0
    g = 1
    while True:
        time.sleep(0)
        inp = input("Letter kopen of woord raden?: ")
        if inp == correct:
            print('\nGefeliciteerd '+naam+'! U heeft het woord geraden!')
            time.sleep(0)
            print("'"+correct+"' geraden na "+str(l)+" letters en "+str(g)+" keer raden.")
            return 'goed',l,g
        elif inp in '1 2 3 4 5 6 7 8 9 10 11 12':
            i = int(inp)-1
            letter = hussel[i]
            hussel = letterverander(hussel,'*',i)
            if letter != '*':
                mogelijkeposities= []
                for j in range(12):
                    if letter == correct[j] and letter != antwoord[j]:
                        mogelijkeposities.append(j)
                pos = random.choice(mogelijkeposities)
                antwoord = letterverander(antwoord,letter,pos)
            print()
            layout(hussel)
            print()
            print()
            layout(antwoord)
            print()
            l += 1
        else:
            print()
            print("Helaas niet het goede antwoord")
            time.sleep(0)
            print()
            layout(hussel)
            print()
            layout(antwoord)
            print()
            g += 1
            

def TweevoorTwaalf():
    print(
    '''
    
            Welkom bij Twee voor Twaalf!
    '''
    )
    naam = ''
    speel = input('\nWilt u spelen? (ja/nee) ')
    if speel == 'ja':
        naam = input('Voer hier uw naam in: ')
        print()
    while speel == 'ja':
        randomwoord = randomwoordpick()
        correct =  randomwoord
        husselwoord = hussel(randomwoord)
        antwoord = '************'
        layout(husselwoord)
        print()
        print()
        layout(antwoord)
        print()
        goed, l, g = raden(husselwoord,antwoord,correct, naam)
        speel = input('\nWilt u nog een keer spelen? ')
        print()
    if naam != '': 
        print('Bedankt om te spelen, '+naam+'!')
    else:
        print('\nBedankt om te spelen!')
    input('\nDruk op de entertoets om af te sluiten.')

TweevoorTwaalf()