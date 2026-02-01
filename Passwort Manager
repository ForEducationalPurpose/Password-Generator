#Passwort Manager für den Generator 
import PasswortGenerator

def SuchenOderNicht():
   print("Passwort Generieren oder nach Passwort suchen? ")
   Antwort = int(input(""))
   if Antwort == 1:
      return True
      exit
   elif Antwort == 2:
      print("You shall now type the Platform")
      Plattform = str(input(""))
      with open('Passwörter.txt', 'r', encoding='utf-8') as file:
       content = file.read()
      if Plattform in content:
        print(f"Das Wort '{Plattform}' wurde gefunden.")
        print(content)
        exit
      else:
        print(f"Das Wort '{Plattform}' wurde nicht gefunden.")
        exit
    
   else:
      print("Error contact @samuelwayo on Discord")
      exit


Platform = str(input("Platform: \n"))
SuchenOderNicht()
if SuchenOderNicht == True:
   Passwort = PasswortGenerator.Generieren
   PasswortGenerator.Speichern
   exit
else:
   ("Error contact @samuelwayo on Discord")
   exit
