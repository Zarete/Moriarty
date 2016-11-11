# -*- coding: utf-8 -*-

import src.Data as Data
import src.Functions as Functions

print("Bienvenue dans ce jeu de Moriarty !")

grid = Functions.create_initial_grid()

Functions.create_player()

print('\nFor this game :'

	'\n 	[+]', Functions.colors.GREEN + Data.current_player['Activator'] + Functions.colors.STOP, 'is the '+Functions.colors.GREEN+'Activator'+Functions.colors.STOP+
	
	'\n 	[+]', Functions.colors.RED + Data.current_player['Inhibitor'] + Functions.colors.STOP, 'is the '+Functions.colors.RED+'Inhibitor\n'+Functions.colors.STOP)


Functions.display_grid(grid)

grid = Functions.playing(Data.current_player['Activator'], grid)

Functions.display_grid(grid)