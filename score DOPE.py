from modeller import *
from modeller.scripts import complete_pdb

# Initialiser l'environnement Modeller
env = environ()
env.libs.topology.read(file='$(LIB)/top_heav.lib')
env.libs.parameters.read(file='$(LIB)/par.lib')

# Lire les 10 modèles précédemment générés
for i in range(1, 11):
    mdl = complete_pdb(env, 'alpha_amy.B9999%04d.pdb' % i)

    # Sélectionner tous les atomes de la première chaîne
    atmsel = selection(mdl.chains[0])

    # Calculer le score DOPE
    score = atmsel.assess_dope()

    # Écrire le score dans un fichier
    with open('score.txt', 'a') as f:
        f.write('Modèle %d : DOPE score = %.3f\n' % (i, score))