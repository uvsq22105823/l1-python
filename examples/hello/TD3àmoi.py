
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

def demandeTemps(j, h, m, s):
    if j<0:
        print("veuillez entrer un nombre valable de jours")
    elif j==1:
        print(j,"jour")
    else:
        print(j,"jours")
    if h>24:
        print("veuillez indiquer un nombre valable d'heures (convertissez en jours)")
    elif h<0:
        print("veuillez indiquer un nombre d'heures valable")
    elif h==1:
        print(h,"heure")
    else:
        print(h,"heures")
    if m>60:
        print("veuillez entrer un nombre valable de minutes ( convertissez en heures etc..)")
    elif m<0:
        print("veuillez entrer un nombre valable de minutes")
    elif m==1:
        print(m,"minute")
    else:
        print(m,"minutes")
    if s>60:
        print("veuillez entrer un nombre valable de secondes ( convertissez en minutes, heures etc...")
    elif s<0:
        print("veuillez entrer un nombre de secondes valable")
    elif s==1:
        print(s,"seconde")
    else:
        print(s,"secondes")
    return

j=int(input("indiquez le nombre de jours\n"))
h=int(input("indiquez le nombre d'heures\n"))
m=int(input("indiquez le nombre de minutes\n"))
s=int(input("indiquez le nombre de seconde\n"))

demandeTemps(j,h,m,s)

