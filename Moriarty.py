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

end = False

while end == False:
	#os.system('clear')

	Functions.display_grid(grid)

	grid, end = Functions.playing(player, grid)

	if player == activator:
		player = Data.current_player['Inhibitor']
	else:
		player = Data.current_player['Activator']


print("OMG THIS IS THE END")

print("##### SCORES #####")
s_activator = 0
s_inhibitor = 0

for elem in grid.values():
	if elem == Functions.colors.GREEN + "[A]" + Functions.colors.STOP:
		s_activator += 1
	elif elem == Functions.colors.RED + "[I]" + Functions.colors.STOP:
		s_inhibitor += 1

if s_activator > s_inhibitor:
	print("\nBRAVO à toi", activator, '!')
else:
	print("\nBRAVO à toi", inhibitor, '!')

print("ACTIVATOR :", s_activator)
print("INHIBITOR :", s_inhibitor)