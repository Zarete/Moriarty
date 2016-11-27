# -*- coding: utf-8 -*-

# Jeu Moriarty

# Author : 

from src import Data as Data
import src.Functions as Functions
import os, sys

# TODO : prendre en compte erreur de choix de l'utilisateur


while True:
	tester = True
	while tester:
		os.system('clear')
		
		Functions.display_menu()
		try:
			choix = int(input("Que voulez vous faire ? "))
		except:
			tester = False
			break

		if choix == 1:
			Functions.get_rules()

		elif choix == 2:
			Functions.PvP()

		elif choix == 3:
			case, no_case = Functions.IA_creating_players()
			Functions.current_game()
			
		elif choix == 4:
			if Data.current_mode[0] == '(Normal)   ':
				Data.current_mode = Data.mode[0]
			else:
				Data.current_mode = Data.mode[1]

		elif choix == 5:
			Functions.quit()
