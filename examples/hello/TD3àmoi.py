
#convertit un temps en jour heure minute secondes en secondes

def tempsEnSeconde(temps):
    jour=int(temps[0]*86400)
    heure=int(temps[1]*3600)
    minute=int(temps[2]*60)
    seconde=int(temps[3])
    nb_secondes=jour+heure+minute+seconde
    return nb_secondes

temps_jhms = (3,23,1,34)
print(type(temps_jhms))
print(tempsEnSeconde(temps_jhms))


#convertit des secondes en jour heures minutes secondes

def secondeEnTemps(tempssecondes):
    jours=int(tempssecondes//86400)
    heures=int((tempssecondes%86400)//3600)
    minutes=int((tempssecondes%3600)//60)
    secondes=int(tempssecondes%60)
    return (jours,heures,minutes,secondes)

temps = secondeEnTemps(100000)
print(temps[0],"jours\n",temps[1],"heures\n",temps[2],"minutes\n",temps[3],"secondes")



#affichage d'un temps


def afficheTemps(tempsobtenu):
    if tempsobtenu[0]>1:
        print(tempsobtenu[0],"jours",end=" ")
    elif tempsobtenu[0]==1:
        print(tempsobtenu[0],"jour",end=" ")

    if tempsobtenu[1]>1:
        print(tempsobtenu[1],"heures",end=" ")
    elif tempsobtenu[1]==1:
        print(tempsobtenu[1],"heure",end=" ")
        

    if tempsobtenu[2]>1:
        print(tempsobtenu[2],"minutes",end=" ")
    elif tempsobtenu[2]==1:
        print(tempsobtenu[2],"minute",end=" ")
    
    
    if tempsobtenu[3]>1:
        print(tempsobtenu[3],"secondes",end=" ")
    elif tempsobtenu[3]==1:
        print(tempsobtenu[3],"seconde",end=" ")
    
    return tempsobtenu
    
tempsrecu=(1,0,14,23)
print(afficheTemps(tempsrecu)) 


#demande et affichage d'un temps

def demandeTemps(demande):
    while True:

        j=int(input("Entre un nb de jours : "))
        if j<=30 and j>=0:
            h=int(input("entre un nb d'heures : "))
        if h<=24 and h>=0:
            m=int(input("entre un nb de minutes : "))
        if m<=60 and m>=0:
            s=int(input("entre un nb de secondes : "))
        if s<=60 and s>=0:
            return print(j,"jour(s)",h,"heure(s)",m,"minute(s)",s,"seconde(s)")
        else:
            print("erreur")
            break
demandeTemps(print)

#additionner deux temps

def sommeTemps(temps1,temps2):
    jours=temps1[0]+temps2[0]
    heures=temps1[1]+temps2[1]
    minutes=temps1[2]+temps2[2]
    secondes=temps1[3]+temps2[3]
    if secondes>60:
        while secondes>60:
            secondes=secondes-60
            minutes=minutes+1
    if minutes>60:
        while minutes>60:
            minutes=minutes-60
            heures=heures+1
    if heures>24:
        while heures>24:
            heures=heures-24
            jours=jours+1
    print(jours,"jours")
    print(heures,"heures")
    print(minutes,"minutes")
    print(secondes,"secondes")
    return
    
sommeTemps((2,3,4,25),(5,22,57,1))
print("/////////////////////////////////////////////////////////////////////////////////////////////////////////")


#proportion d'un temps

def proportionTemps(temps3,proportion):
    nombreDeSecondes=tempsEnSeconde(temps3)
    proportionDeSecondes=nombreDeSecondes*proportion
    tempsResultat=secondeEnTemps(proportionDeSecondes)
    return tempsResultat

temps3=(2,0,36,0)
proportion=(0.2)
print(proportionTemps(temps3,proportion))
