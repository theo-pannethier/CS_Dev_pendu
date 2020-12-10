# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 09:00:56 2020

@author: Utilisateur
"""


from  tkinter import *
import unicodedata
import random



def selection():
    """"programme mettant dans une liste des mots du dictionnaire triés par 
    taille puis par ordre alphabétique.
    Aucune entrée
    Sortie : listes de mots de meme taille (liste)
    
    """
    
    Grande_Liste= open("liste_francais.txt", "r")
    Liste=Grande_Liste.readlines()
    Grande_Liste.close()
    L5=[]
    L6=[]
    L7=[]
    for i in range (len(Liste)):
        taille=len(Liste[i])
        if taille <= 8:
            if taille == 6:
                L5=L5+[Liste[i]]
            elif taille == 7:
                L6=L6+[Liste[i]]
            elif taille == 8:
                L7=L7+[Liste[i]]
        
    return L5,L6,L7


def  creation(pListe_final):
    """fonction creant un fichier texte comprenant tous nos mots triés
    En entrée : liste final comprennant tout les mots liste
    En sortie :rien 
    """
    with open(" Liste_mots.txt", "w") as fichier:
         for i in pListe_final :
             fichier.write(i)
    fichier.close()

    
def selection_mot(pListe_final):
    """" Programme qui trouve et modifie le mot pour jouer
    Entrée : Liste final des mots (liste)
    Sortie : mot en claire pour jouer en str
    """
    i=random.randint(0, len(pListe_final))
    Mot_modif=pListe_final[i][:-1]
    Mot_final= ''.join((c for c in unicodedata.normalize('NFD', Mot_modif ) if 
                        unicodedata.category(c) != 'Mn'))
    print(Mot_final)
    return  Mot_final

def mot_cache(pMot_final):
    """programme permettant de dissimuler le mot à trouver
        Entrée : Mot choisi par la fonction selection_mot str
        Sortie: Mot dissimuler à trouver en str
        """
    Mot_cache= pMot_final[0]
    lettres_restantes=len(pMot_final)-1
    
    for i in range (1,len(pMot_final)):
            if  pMot_final[i] != pMot_final[0]:
                Mot_cache= Mot_cache + "_"
            else:
                Mot_cache=Mot_cache + pMot_final[0]
                lettres_restantes -= 1
    return(Mot_cache,lettres_restantes)


def Gestion_partie (pMot_cache,lettres_restantes,pMot_final):
    """"programme qui gere la partie de pendu:
            nombres de vies
            nombres de lettres restantes 
            Entrée : Mot dissimulé par le programme mot_cache en str
            Sortie : vicoire ou non en booleen
            """
    Lettre_rentree= valuee.get()  
    valuee.set("") 
    lettre =[]
    vie=8
    victoire= False
    lettre.append(lettre_rentree)
    print(lettre)
    Lettre_juste=0
    repetition=1
    if lettre_rentree not in pMot_cache :
        repetition=0
        for i,c in enumerate(pMot_final):
            if c == lettre_rentree  :
                Lettre_juste = 1
                lettres_restantes -= 1
                if i != 0 and i != len(pMot_final)-1:
                    pMot_cache = ( pMot_cache[0:i] + 
                             lettre_rentree + pMot_cache[i+1:] )
                    
                else:
                    pMot_cache = pMot_cache[0:-1] + lettre_rentree 

        if Lettre_juste == 0:
            vie -= 1
            print ("vie",vie)


    elif Lettre_juste == 0 or repetition == 1:
        vie -= 1
        print ("vie",vie)
    print (pMot_cache)

    if lettres_restantes == 0:
        victoire = True
    return victoire,vie


def fin_partie(Liste_final):
    """"programme qui gere la fin de partie de pendu:
        -rejouer
        -donner le score de la partie
    Entrée :Liste_final des mots
    Sortie : score de toutes les  parties jouées à cette session
            mot cache
            """
    i=0 
    serie_victoire=0
    score_session=[]
    score=0
    while i!="1":
        a=selection_mot(Liste_final)
        print(a)
        c,d=mot_cache(a)
        print(c)

        victoire , vie = Gestion_partie(c,d,a)
        if victoire == True:
            serie_victoire += 1
            print(serie_victoire)
            score += serie_victoire*vie
            print(score)
        else:
            serie_victoire = 0
            score_session.append(score)
            score=0
            
        i=input ('voulez vous rejouer (1=non)? : ')
        if i=="1":
            score_session.append(score)

        
    return score_session



def meilleurs_scores(pScore_session):
    """"programme qui gere la fin de partie de pendu:
        -rejouer
        -donner le score de la partie
        Entrée : score_session liste contenant le score de la session 
            terminée
        Sortie : fichier top_score.txt listant les scores par ordre croissant
    """
    
    top_scores= open("top_score.txt", "r")
    liste_scores=top_scores.readlines()
    top_scores.close()
    for i in range(len(liste_scores)):
        liste_scores[i]=int(liste_scores[i][:-1])
    liste_scores.extend(pScore_session)
    liste_scores.sort(reverse=True)
    print(liste_scores)

    for i in range(len(liste_scores)):
        liste_scores[i] = str(liste_scores[i])+'\n'
        

    fichier = open("top_score.txt", "w")
    for i in liste_scores :
             fichier.write(i)

    fichier.close()
    

L5,L6,L7=selection()
Liste_final=L5+L6+L7
(creation(Liste_final))






ma_fenetre=Tk()
ma_fenetre.geometry('1200x650+75+20')
ma_fenetre['bg']='#508CF7'

var = StringVar()
valuee= StringVar()

label = Label( ma_fenetre, textvariable=var, relief=FLAT )


label.pack()

mot = Entry(ma_fenetre, textvariable=valuee, font=("Helvetica", 20) )
mot.pack(side ='left', padx= 100, pady=200)

buttonLettre= Button(ma_fenetre, text = 'Proposer', fg ='#0C9BD2',
                     relief = 'groove', command = lambda :Gestion_partie("z_z_",2,"zozo"))

buttonLettre.pack(side ='left' )



width=300
heigth=300
bonhomme=PhotoImage(file="bonhomme"+str(1)+".gif").zoom(35).subsample(32)
canvas = Canvas(width=width, height=heigth, bg='#4065A4')
canvas.create_image(width/2, heigth/2, image=bonhomme)
canvas.pack(side ='right', padx= 100, pady=100)
ma_fenetre.mainloop()


