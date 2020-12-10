# -*- coding: utf-8 -*-
"""
Programme ou sont repertoriées les fonctions permettant le fonctionnement 
du jeu

Theo Pannethier
03/12/2020
"""


import unicodedata
import random

    
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
    lettre =[]
    vie=8
    victoire= False
    lettre_rentree=input ("quelle lettre : ")
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


    
    
    