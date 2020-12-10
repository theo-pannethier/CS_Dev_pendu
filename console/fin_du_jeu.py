# -*- coding: utf-8 -*-
"""
Programme affichant la victoire/defaite et prpose de rejouer.
Theo Pannethier
03/12/2020
"""
from jeu import *


def fin_partie(Liste_final):
    """"programme qui gere la fin de partie de pendu:
        -rejouer
        -donner le score de la partie
    Entrée :Liste_final des mots
    Sortie : score de toutes les  parties jouées à cette session
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


