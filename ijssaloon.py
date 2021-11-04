import time

print("-------------------------------------------------------------------------")
print(                       "Welkom bij Papi Gelato."                           )
print("-------------------------------------------------------------------------")
time.sleep(1)


#variabelen
hoornBak = 0
Hoorntjes = 0
Bakjes = 0
berekeningBakje = 0
berekeningBolletjes = 0
berekeningHoorntjes = 0

#prijzen 
Geen = float(0.00)
Bak = float(0.75)
Bollen = float(0.95)
Horrentje = float(1.25)
Sprelagroom = float(0.50)
Sprinkles = float(0.30)
CaramelSaus = float(0.60)
Slagroom = float(0.50)

#Doelgroepen
Particulier = "Particulier"
particulier = "particulier"
Zakelijk = "Zakelijk"
zakelijk = "zakelijk"
smaakA = 0
smaakC = 0
#smaakM = 0
smaakV = 0

def snapdatniet():
    print("Sorry dat is geen optie die we aanbieden...")

def doelgroep():
    doelgroep = input("bent u zakelijk of particulier?")
    if doelgroep == "particulier" or doelgroep == "Particulier":
        doelgroep = particulier
        bollensmaak()
    elif doelgroep == "zakelijk" or doelgroep == "Zakelijk":
        doelgroep = Zakelijk
        hoeveelliter()
    else: 
        snapdatniet()

def hoeveelliter():
    liter = input("hoeveel liter ijs wilt u?")
    smaakZakelijk(liter,1)

def smaakZakelijk(liter,literNummer):
    while literNummer <= int(liter):
        global smaakA
        global smaakC
        #global smaakM
        global smaakV
        if literNummer == 1:
            smaakPerLiter = input("Welke smaak wilt u voor de " + str(literNummer) + "st liter? A) Aardbei, C) Chocolade, V) Vanille: ")
            if smaakPerLiter == "A" or smaakPerLiter == "a":
                smaakA = smaakA + 1
                literNummer = literNummer + 1
            elif smaakPerLiter == "C" or smaakPerLiter == "c":
                smaakC = smaakC + 1
                literNummer = literNummer + 1
            elif smaakPerLiter == "V" or smaakPerLiter == "v":
                smaakV = smaakV + 1
                literNummer = literNummer + 1
            #elif smaakPerLiter == "M" or smaakPerLiter == "m":
                #smaakM = smaakM + 1
                #literNummer = literNummer + 1
            else:
                snapdatniet()

        else:
            smaakPerLiter = input("Welke smaak wilt u voor de " + str(literNummer) + "de liter? A) Aardbei, C) Chocolade, V) Vanille: ")
            if smaakPerLiter == "A" or smaakPerLiter == "a":
                smaakA = smaakA + 1
                literNummer = literNummer + 1
            elif smaakPerLiter == "C" or smaakPerLiter == "c":
                smaakC = smaakC + 1
                literNummer = literNummer + 1
            #elif smaakPerLiter == "M" or smaakPerLiter == "m":
               # smaakM = smaakM + 1
                #literNummer = literNummer + 1
            elif smaakPerLiter == "V" or smaakPerLiter == "v":
                smaakV = smaakV + 1
                literNummer = literNummer + 1
            else:
                snapdatniet()
    bonZakelijk()
    
def bonZakelijk():
    global smaakA
    global smaakC
    #global smaakM
    global smaakV
    prijsPerLiter = 9.80
    totaalPrijsLiterA = int(smaakV) * prijsPerLiter
    totaalPrijsLiterC = int(smaakC) * prijsPerLiter
    #totaalPrijsLiterM = int(smaakM) * prijsPerLiter
    totaalPrijsLiterV = int(smaakV) * prijsPerLiter
    btw = 0.09
    totaalPrijs = totaalPrijsLiterA + totaalPrijsLiterC + totaalPrijsLiterV
    btwTotaalPrijs = totaalPrijs * btw
    print("-----------['Papi Gelato']-----------")
    print("")
    if smaakA > 0:
        print("Liter(Aardbei)       " + str(smaakA) + " x €" + str('{0:.2f}'.format(prijsPerLiter)) + "   = €" + str('{0:.2f}'.format(totaalPrijsLiterA)))
    if smaakC > 0:     
        print("Liter(Chocolade)     " + str(smaakC) + " x €" + str('{0:.2f}'.format(prijsPerLiter)) + "   = €" + str('{0:.2f}'.format(totaalPrijsLiterC)))
    #if smaakM > 0:
        #print("Liter(Munt)          " + str(smaakM) + " x €" + str('{0:.2f}'.format(prijsPerLiter)) + "   = €" + str('{0:.2f}'.format(totaalPrijsLiterM)))
    if smaakV > 0:
        print("Liter(Vanille)       " + str(smaakV) + " x €" + str('{0:.2f}'.format(prijsPerLiter)) + "   = €" + str('{0:.2f}'.format(totaalPrijsLiterV)))
    print("                                 ---------")
    print("Totaal                           = €" + str('{0:.2f}'.format(totaalPrijs)))
    print("Btw (9%)                         = €" + str('{0:.2f}'.format(btwTotaalPrijs))) 




def bollensmaak():
    Bollen = input("Hoeveel bolletjes wilt u?")
    Smaak = input()
    if Smaak == "Chocolade" or "Vanille" or "Aardbei":
        print("Toppings: (Geen) | (Slagroom) | (Sprinkels | (CaramelSaus)")
        Topping = input()
        if Topping == "Slagroom":
            Topping = Slagroom
        elif Topping == "Sprinkels":
              Topping = Sprinkles
        elif Topping == "CaramelSaus":
              Topping = CaramelSaus
        elif Topping == "Geen":
              Topping = Geen
        else:
            print("U moet iets anders kiezen !!")

    if Bollen.isdigit() == False:
        print('U kunt alleen getallen kiezen')
    if Bollen <= str(3):
        smaken(Bollen)
        stap2(Bollen)
    elif Bollen <= str(8):
        smaken(Bollen)
        print('Dan krijgt u van mij een bakje met ' + Bollen + ' bolletjes')
        keuze = 'bakje'
        global Bakjes
        Bakjes += 1
        stap3(keuze, Bollen)
    elif Bollen >= str(9):
        print('Sorry, zulke grote bakken hebben we niet')
 
    else:
        print('Sorry dat is geen optie die wij aanbieden')


def smaken(Bollen):
    x = 0
    while x < int(Bollen):
        x += 1
        keuzeSmaak = input('Welke smaak wilt u voor bolletje nummer ' + str(x) + ' ? A Aardbei, C Chocolade of V Vanille? ').lower()
        if keuzeSmaak != 'a' and keuzeSmaak != 'c' and keuzeSmaak != 'v':
            x -= 1
            print('Sorry dat snap ik niet... ')


def hoornBak(keuze):
    if keuze == 'a':
        keuze = 'hoorntje'
        global Hoorntjes
        Hoorntjes += 1
        return keuze
        
    elif keuze == 'b':
        keuze = 'bakje'
        global Bakjes
        Bakjes += 1
        return keuze

def stap2(Bollen):
    keuze = input('Wilt u deze ' + Bollen + ' bollen in A een hoorntje of B een bakje? ').lower()
    if keuze == 'a' or keuze == 'b':   
        if keuze == 'a':
            global Hoorntjes
            Hoorntjes += 1
        else:
            global Bakjes
            Bakjes +=1
        stap3(keuze, Bollen)
        hoornBak(keuze)
    else:
        print('Sorry dat snap ik niet... ')
        stap2(Bollen)     

def stap3(keuze, Bollen):   
    bijbestellen = input('Hier is uw ' + keuze + ' met ' + Bollen + ' bolletje(s). Wilt u nog meer bestellen? (Y/N) ').lower()
    if bijbestellen == 'y':
        bollensmaak()
    elif bijbestellen == 'n':
        bon(Bollen, Bakjes, Hoorntjes, keuze)
        print('\nBedankt en tot ziens!\n')
    else:
        print('Sorry dat is geen optie die we aanbieden...')
        stap3(keuze, Bollen)    

def bon(Bollen, Bakjes, Hoorntjes, keuze):
    prijsBolletjes = float(0.95)
    prijsHorrentje = float(0.75)
    prijsBakjes = float(1.50)
    global berekeningBakje
    global berekeningHoorntjes
    global berekeningBolletjes
    print('\n------------[ Papi Gelato ]------------\n')
    berekeningBolletjes = round(float(Bollen)) * float(prijsBolletjes) 
    print('Bolletjes     =  ' + str(Bollen) + ' x ' + '€' + str(prijsBolletjes) + '  = ' + '€' + str(berekeningBolletjes))
    if Hoorntjes == 0 and Bakjes == 0:
        print('')
    if Hoorntjes > 0:
        berekeningHoorntjes = round(float(Hoorntjes)) * str(prijsHorrentje)
        print('Horrentje     =  ' + str(Hoorntjes) + ' x ' + '€' + str(prijsHorrentje) + ' = ' + '€' + str(berekeningHoorntjes))
    if Bakjes > 0:
        berekeningBakje = round(float(Bakjes)) * str(prijsBakjes)
        print('Bakje         =  ' + str(Bakjes) + ' x ' + '€' + str(prijsBakjes) + ' = ' + '€' + str(berekeningBakje))
    eindbedragCalc = float(berekeningBolletjes) + float(berekeningBakje) + float(berekeningHoorntjes)
    print('\n                           ------------\n')
    print('Totaal                     = ' + str(eindbedragCalc))                       
doelgroep()
                           
