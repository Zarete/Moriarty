# -*- coding: utf-8 -*-

import Data
import Functions

grille = [(x, y) for x in range(8) for y in range(8)]

def players():
	"""Players attribution

	Ask to each player is pseudo and attribute him/her
	a role in the game

	Args : 
		None
	Return :
		return a dictionnary containing the pseudo and role
		of each players"""

	#TODO : Ajout d'une BDD des différents joueurs avec des scores et vérifier la présence des joueurs choisis dans cette BDD pour charger les scores

	activator = ''
	inhibitor = ''

	activator = input("Entrez le pseudo du joueur 'Activator' : ")
	inhibitor = input("Entrez le pseudo du joueur 'Inhibitor' : ")

	return activator, inhibitor
	

print("Bienvenue dans ce jeu de Moriarty !")
activator, inhibitor = players()

print('\nFor this game :'

	'\n[+]', activator, 'is the '+Functions.bcolors.RED+'Activator'+Functions.bcolors.STOP+
	
	'\n[+]', inhibitor, 'is the '+Functions.bcolors.GREEN+'Inhibitor\n'+Functions.bcolors.STOP)



