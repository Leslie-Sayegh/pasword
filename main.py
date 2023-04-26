import hashlib
# Il doit contenir au moins 8 caractères.
# Il doit contenir au moins une lettre majuscule.
# Il doit contenir au moins une lettre minuscule.
# Il doit contenir au moins un chiffre.
# Il doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).
# Voici comment votre programme devrait fonctionner :

#1. Demandez à l'utilisateur de choisir un mot de passe.
#2. Vérifiez si le mot de passe choisi respecte les exigences de sécurité.
#3. Si le mot de passe est valide, affichez un message de confirmation et quittez le programme.
#4. Si le mot de passe n'est pas valide, affichez un message d'erreur et demandez à l'utilisateur de choisir un nouveau mot de passe.
#5. Répétez les étapes 2 à 4 jusqu'à ce que l'utilisateur choisisse un mot de passe valide.

#librairie “Hashlib” utilisant l’algorithme de hachage SHA-256,
#crypte mdp de l'utilisateur (methode césar?)
def password_check(passwd) :
    
    maj = ['A', 'B' 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    chiffres = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    caracterrspecial = ['!', '@', '#', '$', '%', '^', '&', '*']
    val= True

id = input("Identifiant : ")

mdp = input("Mot de passe : ")
mdp1 = "b"

if len(mdp) >= 8 :
    if True in (car in "maj" for car in mdp) :
        if (car in "chiffres" for car in mdp) :
            if (car in "caracterrspecial" for car in mdp) :
                if(mdp1 == ("b")):
                 print ("Bienvenue !!")

else :                  
    print ("Invalid Password !!")
     
    if input("réentrez le mot de passe pour vérifier: ") == mdp:
         confirm = True

 
import hashlib
 
# La chaîne de caractères à hasher
string_to_hash = "example_string"
 
# Création d'un objet hash SHA-256
hash_object = hashlib.sha256()
 
# Mise à jour de l'objet hash avec la chaîne de caractères à hasher
hash_object.update(string_to_hash.encode())
 
# Récupération du hash en hexadécimal
hex_hash = hash_object.hexdigest()
 
print(f"Hash de la chaîne '{string_to_hash}' : {hex_hash}")
#Cela imprimera:
#Hash de la chaîne 'example_string' : 6f1ed002ab5595859014ebf0951522d906a48f094f2f071f2f9b4f5fe809a44
 
if id == "a" and mdp == "b":
    print("Bienvenue")
elif id == "a" and mdp != "b":
    print("Mot de passe incorrect...")
elif id != "a" and mdp == "b":
    print("Identifiant incorrect...")
# tentative=0
#mot_select=''
 
#while tentative < 2:
#   mot=input('Tapez mot de passe: ')
#     
#    if len(mot) >= 8:
#        maj=[c for c in mot if c.isupper()]
#        numb=[c for c in mot if c.isdigit()]
#         
#       if len(maj) > 0 and len(numb) > 0:
#            mot_select=mot
#            break
# 
#    print('Ne respecte pas les règles')
#    tentative+=1
#                     
#if len(mot_select) > 0:
#    print('\n[Mot retenu] > %s.'%mot_select)         