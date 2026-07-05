#Projekt Passwortgenerator
import os
import random
from cryptography.fernet import Fernet



key_file = "secret.key"
if not os.path.exists(key_file):
 key = Fernet.generate_key()
 with open (key_file, "wb") as f:
  f.write(key)
  print("key generated!")
else:
 with open (key_file, "rb") as f:
  key = f.read()
  print("secret key loaded!") 
 
 

cipher = Fernet(key)

def Generieren():
 random.seed()
 platform = input("Platform: \n").encode("utf-8")
 email = input("Deine Email: \n").encode("utf-8")
 Char = "abcdefghijklomnopqrstuvwxyzüöäABCDEFGHIJKLNOPKRSTUFWXYZ123456789!§$%&/())=?.,<?"
 passwort = "".join(random.sample(Char,16))
 print("Das Passwort: ", passwort)
 return passwort, platform, email

passwort, platform, email = Generieren()
print("Platform and Password: \n",platform , "\n", email,"\n", passwort)
passwort = passwort.encode("utf-8")


def Speichern():
 token = cipher.encrypt(passwort)
 token2 = cipher.encrypt(email)
 with open("Passwords.txt", "ab") as f:
  f.write(platform + b"\r\n")
  f.write(token2 + b"\r\n")
  f.write(token + b"\r\n")


Speichern()
