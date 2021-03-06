##import module (tkinter et random)
from tkinter import *
import random

fenetre = Tk()
#variable du jeu
rand = random.randint(1, 100)##génere unn chiffre aleatoire entre 1 & 100
Tab = [ ]
compteur = 0
event = 0 # j'ai déclaré la variable event car le bouton "ok" demande a ce que la variable soit définit et la touche entrée nécessite un 'event' 
      
def jeu(event):##fonction jeu juste prix
    
    global entre, rand, Tab, compteur
    chiffre = entre.get()##recupere la valeur du champs (entre) et met la valeur dans la variable chiffre
    chiffre = int(chiffre)
    
    if chiffre > rand:
        text.set("c'est plus petit")
        entre.delete(0,END)##supprime valeurs champs lorsque la touche entré est préssé
        Tab.append(chiffre)
        test1.set(Tab)##remplace le label
        compteur = compteur+1
    elif chiffre < rand:
        text.set("c'est plus grand")
        entre.delete(0,END)##supprime valeurs champs lorsque la touche entré ou le bouton est préssé
        Tab.append(chiffre)##ajoute valeurs dans le tableau
        test1.set(Tab)##remplace le label
        compteur = compteur+1
 
    else:
        tentative = str(compteur)#conversion de la variable tentative entier en string
        text.set("bravo tu as trouvé en "+tentative+" coup \n le nombre était " + str(rand))
        global rejouer#variable du bouton rejouer
        rejouer = Button(fenetre, text="REJOUER", command=restart)##creation du bouton rejouer
        rejouer.pack(pady = 15)##affiche le bouton
        
##titre
titre = Label(fenetre, text="JUSTE PRIX", font=("Ubuntu", 40))
fenetre.geometry("1080x720")##dimention de la fenetre
fenetre.resizable(width=False, height=False)##block la redimention de la fenetre
fenetre.title("JUSTE_PRIX")
titre.pack(pady = 30)

##input (saisie)
instruction = Label(fenetre, text="Veuillez ecrire un chiffre entre un et 100  :")
instruction.pack(pady = 30)##Affiche l'instruction
entre = Entry(fenetre)##Creation d'un champ (input)
entre.pack(pady = 20)##Affiche le champ

##bouton
fenetre.bind('<Return>',jeu)##Action de la touche entrer
bouton = Button(fenetre, text="OK", command=lambda : jeu(event))##creation du bouton faisant appel a la fonction jeu (lambda spécifie que la foction a un argument 'event')
bouton.pack(pady = 15)##affiche le bouton

#affichage resultat
text = StringVar()
text.set("GOOD LUCK !")
result = Label(fenetre, textvariable=text, font=("Courier", 22))##crée un label result qui sera modifié a l'aide de la fonction
result.pack(pady=50)##affiche le label result

##affichage chiffre entré
test1 = IntVar()##Initialise la variable Test1
test2 = Label(fenetre, textvariable=test1, font=("Ubuntu", 35))##crée un label result qui sera modifié a l'aide de la fonction
test2.pack(pady = 10)##affiche le label result

def restart():
    global rand#la variable devient global 
    rand = random.randint(1, 100)##génere unn chiffre aleatoire entre 1 & 100
    entre.delete(0,END)##supprime valeurs champs lorsque la touche entré est préssé
    text.set("GOOD LUCK !")
    del Tab[:]##supprime l'integralite de la liste
    test1.set(Tab)##met a jour Tab
    test2.pack(pady = 30)##affiche le label result
    Button.destroy(rejouer)

##Menubar
menubar = Menu(fenetre)
fenetre.config(menu=menubar)
menufichier = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Fichier", menu=menufichier)
menufichier.add_command(label="Recommencer", command=restart)
menufichier.add_command(label="Quitter", command=fenetre.destroy)

##couleurs
fenetre.config(bg="black")
titre.config(fg="#FFFFFF")
titre.config(bg="black")
instruction.config(fg="#FFFFFF")
instruction.config(bg="black")
result.config(fg="#FFFFFF")
result.config(bg="black")
test2.config(fg="#FFFFFF")
test2.config(bg="black")

fenetre.mainloop()#permet d'afficher la fenetre constament 












        
    




