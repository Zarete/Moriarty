# -*- coding: utf-8 -*-

"""CHOIX DE PIONS DE FORMES DIFFERENTES POUR EVITER LES PROBLEMES
   DE DALTONISME -> CHOIX A FAIRE (METTRE DANS RAPPORT)"""

import src.Data as Data
import src.Functions as Functions
from random import choice
import os

os.system('clear')

print(Functions.colors.HEADER + "			Bienvenue dans ce jeu de Moriarty !" + Functions.colors.STOP)

grid = Functions.create_initial_grid()

activator, inhibitor = Functions.create_player()

player = choice([activator, inhibitor])

print('\nFor this game :'

	'\n 	[+]', Functions.colors.GREEN + activator + Functions.colors.STOP, 'is the '+Functions.colors.GREEN+'Activator'+Functions.colors.STOP+
	
	'\n 	[+]', Functions.colors.RED + inhibitor + Functions.colors.STOP, 'is the '+Functions.colors.RED+'Inhibitor\n'+Functions.colors.STOP)

while True:

	#os.system('clear')

	Functions.display_grid(grid)

	grid = Functions.playing(player, grid)

	if player == activator:
		player = Data.current_player['Inhibitor']
	else:
		player = Data.current_player['Activator']
