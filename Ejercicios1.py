import math
a=input("Dis-moi ton âge: ")
cosa=math.cos(int(a))
sina=math.sin(int(a))
print("Le cosinus de ton âge est {:1.5f}.".format(cosa))
print("Le sinus de ton âge est {:1.5f}.".format(sina))

b=input("Dis-moi le mois de ton anniversaire (nombre) : ")
b1=input("Maintenant, dis-moi le jour: ")
complejo=complex(int(b),int(b1))
mod=(abs(complejo))**2
print("Le numéro complexe créé avec la date de votre anniversaire est: ", complejo)
print("Le carré du module dudit nombre est :", mod)

e1=int(input("Dis-moi un nombre: "))
e2=int(input("Dis-m'en un autre: "))
e3=int(input("Et un autre: "))
e4=int(input("Et un autre: "))
e5=int(input("Le dernier, s'il te plaît: "))
print("Nombre | Carrée".format(e1, e1**2))
print("   {}   |   {}  ".format(e1, e1**2))
print("   {}   |   {}  ".format(e2, e2**2))
print("   {}   |   {}  ".format(e3, e3**2))
print("   {}   |   {}  ".format(e4, e4**2))
print("   {}   |   {}  ".format(e5, e5**2))

f=int(input("Dis-moi ta taille (en centimètres): "))
f1=math.sqrt(f)
print("La racine carrée de votre taille est: {} cm.".format(f1))

g=input("Dis-moi le mot le plus long que tu connais: ")
print("Jajaja... Ça semble étrange lorsqu’il est lu à l’envers, n’est-ce pas?",g[::-1])

h=input("Quelle est la personne que vous aimez le plus?: ")
print("¡¡¡¡ÉPOUSE-MOI, {}!!!".format(h.upper()))