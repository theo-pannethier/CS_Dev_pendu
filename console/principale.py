# -*- coding: utf-8 -*-
"""

Programme principale du pendu.
Theo Pannethier
03/12/2020

https://github.com/theo-pannethier/CS_Dev_pendu.git
"""


from fin_du_jeu import fin_partie
from fin_du_jeu import meilleurs_scores

from creation_liste import selection
from creation_liste import creation




L5,L6,L7=selection()
Liste_final=L5+L6+L7
(creation(Liste_final))

score=fin_partie(Liste_final)
meilleurs_scores(score)


