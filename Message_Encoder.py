#-----------------------------------------------------------------------------------------
"""
#  #  ####   ##    ##    ##    ##   ####        ####  #  #   ##    ##   ###   ####  ###
####  #     #  #  #  #  #  #  #  #  #           #     ## #  #  #  #  #  #  #  #     #  #
####  ###    #     #    #  #  #     ###         ###   ## #  #     #  #  #  #  ###   #  #
#  #  #       #     #   ####  # ##  #           #     # ##  #     #  #  #  #  #     ###
#  #  #     #  #  #  #  #  #  #  #  #           #     # ##  #  #  #  #  #  #  #     # #
#  #  ####   ##    ##   #  #   ###  ####        ####  #  #   ##    ##   ###   ####  #  #
"""
#------------------------------------------------------------------------------------------

"""importation des bibliothèques utilisées dans le code"""
from tkinter import *#on importe la bibliothèque tkinter (affichage)
import unicodedata # A ne pas oublier pour le formattage du texte (fonctions retire accent)

"""création de la fenêtre"""
window = Tk()  #on définit une fenêtre appelée window

"""paramètres de la fenêtre"""
window.title("Message Encoder")  #titre de la fenetre
window.geometry("1400x970")       #taille de la fenetre générée
window.config(background='#202124') #couleur de fond

"""Ajouter titre"""
label_titre = Label(window, text="Bienvenue sur Message Encoder !", font=("Arial", 30), bg='#202124', fg= "#ffffff",bd=3)  #défini un label (titre)
label_titre.grid(row=1,column=0, columnspan=25,pady=10)   #affiche ce label

"""PARTIE CESAR"""
label_soustitre = Label(window, text="Ici, vous pouvez coder votre message en chiffrement avec le code de césar:", font=("Arial", 15), bg='#202124', fg= "white")
label_soustitre.grid(row=2, column=0)  #label de la partie césar

"""1-champs de saisie du message à traduire"""
chaine_c = StringVar() #la valeur de chaine est modifiée en direct, (pas quand on écrit chaine=...)
chaine_c.set("quel message souhaitez vous traduire ?") #on définit un texte par défaut pour chaine_c
entree = Entry(window, width=60, bg="#303134", fg="white", bd=0, font=("Arial", 13), textvariable=chaine_c)
entree.grid(row=3, column=0, pady=25,ipady=3)#barre de saisie(Entry)du texte que l'on veut traduire

"""2-champs de saisie du pas (décalage)"""
clef = StringVar() #la valeur de chaine clef est modifiée en direct, (pas quand on écrit chaine=...)
clef.set("quelle est la clé de décalage que vous souhaitez utiliser ? (ex: 2)") #chaine qui s'affiche dans l'entry
entree_c = Entry(window, textvariable=clef, width=60, bg="#303134", fg="white", bd=0, font=("Arial", 13))
entree_c.grid(row=4, column=0,pady=25,ipady=3)#barre de saisie (Entry) du chiffre de decal.

#---------------------------TRADUCTION DU MESSAGE EN CESAR ---------------------------------

"""fonctions qui convertissent le texte de manière à obtenir une chaine de caractère en majuscule sans accents ni ponctuation"""

alphabet="azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN"

def retireLesAccents(s):  #FONCTION QUI RETIRE LES ACCENTS DE LA CHAINE
    texte= ''.join((c for c in           unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))
    return texte

def retireEspPonct(texte): #FONCTION QUI RETIRE LES ESPACES ET LA PONCT. DE LA CHAINE
    rep=""
    for car in texte:
        if car in alphabet:
            rep=rep+car
    return (rep)

def majusc(texte):   #FONCTION QUI MET LE TEXTE ENTIEREMENT EN MAJUSCULE
    rep=""
    for car in texte:
        if ord(car)<91:
            nouvcar=car
        else:
            nouvcar = chr(ord(car)-32)
        rep=rep+nouvcar
    return(rep)

def formateTexte(texte):#FONCTION APPLIQUE LES TROIS FONCTIONS SUR LE TEXTE DE L UTILISATEUR
    texte=retireLesAccents(texte)
    texte=retireEspPonct(texte)
    texte=majusc(texte)
    return(texte)

"""FIN DES FONCTIONS QUI FORMATENT LE TEXTE"""

"""Clé de décalage"""
#fonction qui qui prend la chaine de caractere étant un chiffre (ex: "3") rentrée par l'utilisateur et qui la convertit en entier avec int() (ex: "3" devient 3) sa valeur n'est plus chaine de caractère mais bien entier

def clefCesar(clef):
    cle=int(clef)
    return cle

"""Traduction en césar"""
#cette fonction prend le texte entré par l'utilisateur, le formate par les fonctions de formatages définies au dessus.
def cesar():
    res=""
    texte=chaine_c.get()
    texte=formateTexte(texte)
    print(texte)
    print(entree_c.get())
    clef=clefCesar(entree_c.get())
#puis pour chaque caractère de ce texte elle vérifie la condition si le code ASCII du caractère + la clef>90. si oui alors la réponse sera la transformation en caractère (chr) du  code ASCII de chaque caractère + la clef - 26 (alphabet) Sinon, la réponse sera la même mais on ne va pas soustraire 26.
    for car in texte:
        clef=int(clef)
        if ord(car)+clef>90:
            res=res+chr(ord(car)+clef-26)
        else:
            res=res+chr(ord(car)+clef)
    print(res)
    entry_response_c.delete(0,END)   #permet de supprimer la valeur présente dans entry_response_c
    entry_response_c.insert(0,res)   #puis d'insérer la valeur de res dans entry_esponse_c pour l'afficher

    #j'ai choisi d'afficher mes réponses dans des entry et non des Labels car + simple pour les fonctions de copies

#bouton traduire qui appelle la fonction césar avec command=cesar
button = Button(window, text=" Crypter mon message 🔒",font=("Arial", 15), bg='white', fg= "#2E2E2E", cursor="hand1", overrelief=RIDGE, activebackground='#2E2E2E', activeforeground="white", command=cesar)
button.grid(row=5, pady=25) #affichage du bouton
#affichage du résultat
entry_response_c = Entry(window, width=60, bg="#303134", fg="white", bd=0, font=("Arial", 13)) #definition de l'entry de reponse
entry_response_c.grid(row=6, column=0, pady=25,ipady=3) #affichage de cette réponse

"""copie du texte dans le presse papier de l'utilisateur"""
def mess_copie_c(duration=2000): #fonction d'affichage du message "Message copié avec succès !" lors de la copie, "duration" est le temps d'affichage du message "Message copié avec succès !" Une fois ce temps écoulé, le message (Label) sera détruit avec ".destroy"
    label_copie = Label(window, text="Message copié avec succès !", font=("Arial", 15), bg='#202124', fg= "white")
    label_copie.grid(row=8, column=0)
    label_copie.after(duration, label_copie.destroy)

#fonction de copie qui prend la réponse affichée dans l'entry et qui la copie dans le presse-papier de l'utilisateur
def copie_c(): # fonction qui permet la copie du message avec ".clipboard_clear" qui va supprimer la chaine stockée dans les presse papier de l'utilisateur et .clipboard_append(la réponse) qui va stocker dans le presse papier de l'utilisateur la réponse renvoyée.
    entry_response_c.clipboard_clear()
    entry_response_c.clipboard_append(entry_response_c.get())

def copie_message_c(): #comme un bouton ne peut prendre qu'une fonction en commande, on définit une 3e fonction qui execute les 2 dernières afin d'avoir une seule fonctio en commande mais qui en appelle 2.
    copie_c()
    mess_copie_c()

#bouton copier
copy_button_c=Button(text="copier le texte dans le presse papier", font=("Helvetica", 15),  bg='white', fg= "#2E2E2E", cursor="hand1", overrelief=RIDGE, activebackground='#2E2E2E', activeforeground="white", command=copie_message_c)  #création du bouton
copy_button_c.grid(row=7, column=0) #affichage

#--------------------------------------------TRADUCTION EN CESAR TERMINEE-----------------------------------------------

"""PARTIE VIGENERE"""
#soustitre qui affiche que nous abordons la partie traduction Vigenere
label_soustitre = Label(window, text="Ici, vous pouvez coder votre message en chiffrement avec le code de Vigenère :", font=("Arial", 15), bg='#202124', fg= "white") #création du label
label_soustitre.grid(row=9, column=0, pady=25) #affichage du label

#champs de saisie du message à traduire
chaine_v = StringVar() #la valeur de chaine est modifiée en direct, (pas quand on écrit chaine=...) Attention il existe déjà une variable chaine donc on lui a donné un autre nom
chaine_v.set("quel message souhaitez vous traduire ?") #valeur qui s'affiche par défaut
entree1_v = Entry(window, textvariable=chaine_v,width=60, bg="#303134", fg="white", bd=0, font=("Arial", 13))
entree1_v.grid(row=10, column=0, pady=25,ipady=3)

"""" #champs de saisie du pas (décalage)"""
clef_v = StringVar() #la valeur de chaine est modifiée en direct, (pas quand on écrit chaine=...)
clef_v.set("quelle est la clé que vous souhaitez utiliser ? (ex: CLE)")
entree2_v = Entry(window, width=60, bg="#303134", fg="white", bd=0, font=("Arial", 13), textvariable=clef_v)
entree2_v.grid(row=11, column=0,pady=25, ipady=3)

#------------------------------------------TRADUCTION DU MESSAGE EN VIGENERE--------------------------------------------
#Cle de vigenere
def clefVigenere(clef_v): # fonction qui va dire que la clé est égale à la valeur entrée par l'user dans le champs défini pour cette clé.
    clef_v=entree2_v.get()
    return clef_v

#(pour la fonction du dessous) Traduction en chiffrement Vigenère,après avoir formatté le texte avec les fonctions de formatages définies plus tôt, cette fonction, pour chaque caractère du texte, pendant la longueur du texte va définir une réponse qui sera égale à la valeur chr de l'addition de chaque ord de caractère + chaque ord de la clé, -130 pour remettre le code dans l'alphabet (65 pour chaque ord donc x2 car on en 2 donc 130). on prend le reste de la division euclidienne par 26 (nbre de lettres dans l'alphabet) +65 pour remettre le code ASCII dans les valeurs comprises entre 65 et 90 pour obtenir un message en majuscule et donc afficher les lettres corssepondantes avec le chr du début permettant donc d'obtenir une chaine de caractère.

def Vigenere():
    texte=chaine_v.get()
    texte=formateTexte(texte) #on rappelle la fonction qu'on avait défini pour césar
    resp_v=""
    clef_v=clefVigenere(entree2_v.get())
    for i in range (len(texte)):
        resp_v=resp_v+chr((((ord(texte[i])+ord(clef_v[i%len(clef_v)]))-130)%26)+65)
    print(resp_v)
    entry_response_v.delete(0,END) #permet de supprimer la valeur présente dans entry_response_c
    entry_response_v.insert(0,resp_v) #puis d'insérer la valeur de res dans entry_esponse_c pour l'afficher

#--------------------------------------TRADUCTION EN VIGENERE TERMINEE-----------------------------------------

#bouton traduire
button = Button(window, text="Crypter mon message 🔒",font=("Arial", 15), bg='white', fg= "#2E2E2E", cursor="hand1", overrelief=RIDGE, activebackground='#2E2E2E', activeforeground="white", command=Vigenere) #création du bouton
button.grid(row = 12, pady=25) # affichage du bouton

#resultat
entry_response_v = Entry(window, width=60, bg="#303134", fg="white", bd=0, font=("Arial", 13)) #création de l'entry
entry_response_v.grid(row=13, column=0, pady=25, ipady=3) #affichage de l'entry

"""copie du texte dans le presse papier de l'utilisateur"""
#fonction de copie (même que celle de césar mais avec la chaine de l'entry Vigenere

def mess_copie_v(duration=2000): #même fonction que le copie de césar
    label_copie = Label(window, text="Message copié avec succès !", font=("Arial", 15), bg='#202124', fg= "white")
    label_copie.grid(row=15, column=0)
    label_copie.after(duration, label_copie.destroy)

def copie_v(): #même fonction que le copie de césar
    entry_response_v.clipboard_clear()
    entry_response_v.clipboard_append(entry_response_v.get())

def copie_message_v(): #même fonction que le copie de césar
    copie_v()
    mess_copie_v()

#bouton copier
copy_button_v=Button(text="copier le texte dans le presse papier", font=("Arial", 15), bg='white', fg= "#2E2E2E", cursor="hand1", overrelief=RIDGE, activebackground='#2E2E2E', activeforeground="white", command=copie_message_v) #création du bouton
copy_button_v.grid(row=14, column=0) #affichage du bouton

"""PARTIE BRUTEFORCE DE CESAR"""

label_soustitre = Label(window, text="Ici, vous pouvez déchiffrer votre message chiffré avec la bruteforce attaque:", font=("Arial", 15), bg='#202124', fg= "white") #création du label
label_soustitre.grid(row=2, column=1) #affichage du label

label_warning = Label(window, text="(Pour que le message puisse être clairement décrypté, veuillez utiliser un message plutôt long)", font=("Arial", 10), bg='#202124', fg= "white") #création du label
label_warning.grid(row=3, column = 1) #affichage du label

chaine_bfc = StringVar() #la valeur de chaine est modifiée en direct, (pas quand on écrit chaine=...)
chaine_bfc.set("Quel est le message que vous souhaitez decrypter ? (en majuscule)") #message affiché par défaut dans la chaine
entree_bfc = Entry(window, textvariable=chaine_bfc, width=60, bg="#303134", fg="white", bd=0, font=("Arial", 13)) #création de l'entry affichant la chaine
entree_bfc.grid(row=4, column=1,pady=15, ipady=3) #barre de saisie (Entry) du mdp que l'user souhaite déchiffrer, affichage de cette barre

#fonction qui va craquer le code de césar et nous faire obtenir la clé de décalage et donc le message codé à partir de statistiques,

alph="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def decalage(text):
    indices=[0]*26
    for car in text:
        indices[alph.index(car)]=indices[alph.index(car)]+1
    imax=0
    max=indices[0]
    for i in range(1,len(indices)):
        if indices[i]>max:
            max=indices[i]
            imax=i
    return imax-4

"""DEFINITION D'UN ENTRY POUR LA REPONSE"""
entree_responsebfc = Entry(window, width=60, bg="#303134", fg="white", bd=0, font=("Arial", 13)) #création de l'entry de réponse
entree_responsebfc.grid(row=6, column=1, ipady=3) # affichage de la réponse

def Cesar(text,n): #2e fonction césar qui sert juste pour le bruteforce. on ne peut pas reprendre celle du dessus car elle marche spécialement avec les entry correspondant à la partie de traduction en césar
    res=""
    for car in text:
        res=res+chr(((ord(car)+n-65)%26)+65)
    return(res)


def decode(): #fonction sans paramètre pour qu'elle puisse être affectée au bouton qui appelle César
   text2=entree_bfc.get()
   entree_responsebfc.delete(0,END)
   entree_responsebfc.insert(0,Cesar(text2,26-decalage(text2)))

"""DEFINITION DU BOUTON POUR DECODER"""
button = Button(window, text="Décrypter mon message 🔓",font=("Arial", 15), bg='white', fg= "#2E2E2E",  cursor="hand1", overrelief=RIDGE, activebackground='#2E2E2E', activeforeground="white", command=decode)#création deu bouton
button.grid(row=5, column=1, pady=25) # affichage du bouton


#affichage de la fenêtre
window.mainloop()

#----------------------------------------CONTACT ME-------------------------------------------------#
#contact me: slzr.tech@gmail.com
#MADE BY SLZR








