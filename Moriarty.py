# -*- coding: utf-8 -*-

import src.Data as Data
import src.Functions as Functions

grid = [{(x,y) : ' * ' } for y in range(8) for x in range(8)]

print("Bienvenue dans ce jeu de Moriarty !")

activator, inhibitor = Functions.player_definition()

print('\nFor this game :'

	'\n[+]', activator, 'is the '+Functions.colors.RED+'Activator'+Functions.colors.STOP+
	
	'\n[+]', inhibitor, 'is the '+Functions.colors.GREEN+'Inhibitor\n'+Functions.colors.STOP)

Functions.display_grid(grid)
