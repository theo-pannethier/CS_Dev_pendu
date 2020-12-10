# -*- coding: utf-8 -*-
"""
ce programme permet de creer notre fichier texte contenant 1000 mots à partir
d'un fichier texte de 36000 mots et de le trier.
Theo Pannethier
03/12/2020
"""

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
    

L5,L6,L7=selection()
Liste_final=L5+L6+L7
creation(Liste_final)

