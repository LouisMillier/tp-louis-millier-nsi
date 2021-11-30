from math import sqrt


a = float(input("Saisissez la valeur a "))
b = float(input("Saisissez la valeur b "))
c = float(input("Saisissez la valeur c "))

def discriminant(a,b,c):
    delta =(b**2) - (4*a*c)
    return delta

def equation (a,b):
    delta = discriminant (a,b,c)

    if a == 0:
        texte = " Erreur: a ne peut pas être égale à 0."
    else :
        if delta < 0:
            texte = "L'équation ne comporte aucune solutions."
        elif delta == 0:
            texte = " Les solutions de l'équation sont " + str((-b)/2*a)

        elif delta > 0:
            x1 = ((-b)- sqrt(delta))/2*a
            x2 = ((-b )+ sqrt(delta))/2*a
            texte = "Les solutions de l'équation sont" + str(x1) + " et "+str(x2)
    return texte


print(equation(a,b,c))



