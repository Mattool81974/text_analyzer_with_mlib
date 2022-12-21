import time

from MLib import *
from time import *

TAILLE=(500, 500)

fenetre=display.set_mode(TAILLE)
app = MFenetre(fenetre, "Mon app")
titre = MTexte("Analyseur de texte", (100, 0), (300, 100), app, policeTaille=43, bordureLargeur=2, arrierePlanCouleur=(255, 0, 0))
#titreTexte = MTexte("Texte:", (0, 100), (100, 150), app, policeTaille=30)
#titreChar = MTexte("Caractère:", (0, 250), (225, 50), app, policeTaille=30)

while True:
    app.frame()

    sleep(0.05)

    display.flip()