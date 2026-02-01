#Projekt Passwortgenerator
import random



def Generieren():
 random.seed()
 Char = "abcdefghijklomnopqrstuvwxyzüöäABCDEFGHIJKLNOPKRSTUFWXYZ123456789!§$%&/())=?.,<?"
 Passwort = "".join(random.sample(Char,16))
 return Passwort
 
Passwort = str(Generieren())


def Speichern():
 with open("Passwörter.txt", "a", encoding="utf-8") as datei:
  Platform = str(input("Platform: \n"))
  datei.write(Platform + "\n")
  datei.write(Passwort + "\n")


Speichern()
