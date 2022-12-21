from MLib import *

TAILLE=(500, 500)

fenetre=display.set_mode(TAILLE)
app = MFenetre(fenetre, "Mon app")

while True:
    app.frame()
    display.flip()