from cryptography.fernet import Fernet
key_file = "secret.key"
def secretkey():
    #Loading secret key
    with open(key_file, "rb") as f:
        key = f.read()
        print("secret key loaded!")
    
    cipher = Fernet(key)
    return cipher

cipher = secretkey()

def searchandecrypt():
    asking_platform = input("platform: \n").encode("utf-8") #perfect spelling needed wont work otherwise
    with open("Passwords.txt", "rb") as f:
        zeilen = f.readlines()
        for i in range(0, len(zeilen), 3):   
            platform = zeilen[i]
            email = zeilen[i+1]
            password = zeilen[i+2]
            if platform.strip().decode("utf-8") == asking_platform.decode("utf-8"):  
                decrypted_email = cipher.decrypt(email.strip()).decode("utf-8") #decrypts the found email and cuts the \r\n also decodes it from bytes to str
                decrypted_password = cipher.decrypt(password.strip()).decode("utf-8") #same again fernet doesnt like to decrypt two at the same time
                print(f"The Platform: {platform.strip()}")
                print(f"The Email: {decrypted_email}")
                print(f"The Password: {decrypted_password}")

searchandecrypt()
