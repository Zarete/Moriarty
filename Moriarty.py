# -*- coding: utf-8 -*-

# Jeu Moriarty

# Author : 

from src import Data as Data
import src.Functions as Functions
from random import choice
import os, sys


while True:
	os.system('clear')
	
	Functions.display_menu()

	choix = int(input("Que voulez vous faire ? "))

	if choix == 1:
		Functions.get_rules()

	elif choix == 2:
		os.system('clear')

		print(Functions.colors.HEADER + "			Bienvenue dans ce jeu de Moriarty !" + Functions.colors.STOP)

		grid = Functions.create_initial_grid()

		Functions.create_player()

		player = choice([Data.current_player['Activator'], Data.current_player['Inhibitor']])
		print(player)

		print('\nPour cette partie :'

			'\n 	[+]', Functions.colors.GREEN + Data.current_player['Activator'] + Functions.colors.STOP, 'is the '+Functions.colors.GREEN+'Activator'+Functions.colors.STOP+
			
			'\n 	[+]', Functions.colors.RED + Data.current_player['Inhibitor'] + Functions.colors.STOP, 'is the '+Functions.colors.RED+'Inhibitor\n'+Functions.colors.STOP)

		stop = False
		retry = ''
		end = False

		while not stop:

			while not end:
				os.system('clear')

				grid, end = Functions.playing(player, grid)

				if player == Data.current_player['Activator']:
					player = Data.current_player['Inhibitor']
				else:
					player = Data.current_player['Activator']


			print("FIN DE LA PARTIE")

			print("##### SCORES #####")
			s_activator, s_inhibitor = Functions.get_score(grid)

			if s_activator > s_inhibitor:
				print("\nFélicitation", Data.current_player['Activator'], '! Tu as gagné cette manche avec un score de ', s_activator, '... mais as-tu gagné la guerre ?')
			else:
				print("\nFélicitation", Data.current_player['Inhibitor'], '! Tu as gagné cette manche avec un score de ', s_inhibitor, '... mais as-tu gagné la guerre ?')

			print("Score de ", Data.current_player['Activator'], '(ACTIVATOR)', s_activator)
			print("Score INHIBITOR :", Data.current_player['Inhibitor'], '(INHIBITOR)', s_inhibitor)

			try:
				retry = str(input(" Voulez-vous faire une nouvelle partie ? (O/N)\n Choix : ")).upper()

				if retry not in ['O', 'N']:
					raise ValueError
				elif retry == 'O':
					stop = False
				else:
					stop = True

			except ValueError:
				print("\n  [+] Veuillez entrer une réponse correcte (O/N)")

	elif choix == 3:
		pass

	elif choix == 4:
		if Data.current_mode[0] == '(Normal)   ':
			Data.current_mode = Data.mode[0]
		else:
			Data.current_mode = Data.mode[1]

	elif choix == 5:
		os.system('clear')
		print("""
		d888888b db   db  .d8b.  d8b   db db   dD   db    db  .d88b.  db    db 
		   88    88   88 d8' `8b 888o  88 88 ,8P'   `8b  d8' .8P  Y8. 88    88 
		   88    88ooo88 88ooo88 88V8o 88 88,8P      `8bd8'  88    88 88    88 
		   88    88   88 88   88 88 V8o88 88`8b        88    88    88 88    88 
		   88    88   88 88   88 88  V888 88 `88.      88    `8b  d8' 88b  d88 
		   YP    YP   YP YP   YP VP   V8P YP   YD      YP     `Y88P'   Y8888P  
		                                                                       
		                                                                       
		d88888b  .d88b.  d8888b. 
		88'     .8P  Y8. 88  `8D 
		88ooo   88    88 88oobY' 
		88      88    88 88`8b   
		88      `8b  d8' 88 `88. 
		YP       `Y88P'  88   YD 
		                         
		                         
		d8888b. db       .d8b.  db    db d888888b d8b   db  d888b    db 
		88  `8D 88      d8' `8b `8b  d8'   `88'   888o  88 88' Y8b   88 
		88oodD' 88      88ooo88  `8bd8'     88    88V8o 88 88        YP 
		88      88      88   88    88       88    88 V8o88 88  ooo      
		88      88booo. 88   88    88      .88.   88  V888 88.  8    db 
		88      Y88888P YP   YP    YP    Y888888P VP   V8P  Y888P    YP \n\n""")
		sys.exit()

"""choix = 0
while choix not in range(1, 6, 1):
	try:
		choix = input("Que voulez vous faire ? ")
		if choix not in range(1,6,1):
			raise ValueError
	except ValueError:
		print("Option non disponible")"""
