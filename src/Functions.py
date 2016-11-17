# -*- coding: utf-8 -*-

from . import Data as Data
import os

# Add colors into the terminal
class colors:
	STOP = '\033[0m'
	BOLD = '\033[1m'
	HEADER = '\033[95m'
	HEADERB = BOLD + '\033[95m'

	GREEN = BOLD + '\033[92m'
	GREENB = '\033[42m'

	RED = BOLD + '\033[91m'
	REDB = '\033[41m'


def display_menu():
	"""Display the menu

	Display the menu of the game with de different options

	Args : 
		None
	Return : 
		None"""

	print("""
"""+colors.BOLD+"""
                              __  __            _            _                          
                             |  \/  |          (_)          | |                         
                             | \  / | ___  _ __ _  __ _ _ __| |_ _   _                  
                             | |\/| |/ _ \| '__| |/ _` | '__| __| | | |                 
                             | |  | | (_) | |  | | (_| | |  | |_| |_| |                 
                             |_|  |_|\___/|_|  |_|\__,_|_|   \__|\__, |                 
                                                                  __/ |                 
                                                                 |___/                  
"""+colors.STOP+"""
		╒================================================================╕
		│                                                                │
		│    ◈ 1 ◈ Afficher les règles du jeu                            │
		│                                                                │
		│                                                                │
		│    ◈ 2 ◈ Joueur vs Joueur                                      │
		│                                                                │
		│                                                                │
		│    ◈ 3 ◈ Joueur vs Ordinateur                                  │
		│                                                                │
		│                                                                │
		│    ◈ 4 ◈ Mode d'affichage                                      │
		│              """+Data.current_mode[0]+"""                                       │
		│                                                                │
		│    ◈ 5 ◈ Quitter                                               │
		│                                                                │
		╘================================================================╛

""")

def get_rules():
	"""Display informations about the game

	Display the rules and informations for the game Moriarty, a long description is made in this function and
	displayed on the screen

	Args :
		None
	Return :
		None"""

	os.system('clear')
	print("""
	Le but du jeu est d'incarner le rôle d'un activateur ou d'un inhibiteur
	protéique. Ainsi au début du jeu chaque joueur choisis un rôle afin de
	commencer la partie. Dans notre cas le rôle d'activateur pose des pions
	de couleur verte et l'inhibiteur en pose de la couleur rouge.
	Ces différents pions ont la possibilité de changer d'état en fonction de
	leur environnement.

	Règles du jeu :
		Quand une ou plusieurs protéines vertes sont encadrés par 2 pions de la
		couleur rouge les protéines vertes passent dans l'état inhibiteur (rouge),
		et inversement pour les protéines rouges vis à vis des vertes.
		Cet encadrement est valable dans toutes les directions de l'espace.

	Déroulement d'une manche :
		Le joueur pose un pion dans une case. Plusieurs règles sont à respecter :
			[+] Le pion ne peut être posé dans une case déjà occupée
			[+] Le placement du pion doit induire le changement de statut d'au moins un pion adverse
		Les manches se suivent en respectant ces deux conditions.

	Fin du jeu :
		La fin du jeu survient quand un des joueurs ne peut plus poser de pions.
		S'ensuit le calcul des scores et la désignation du vainqueur.

	Score :
		Les scores correspondent au nombre de pions de chaque couleur sur l'ensemble
		de la grille.
		Le vainqueur est celui qui présente le plus de points, donc de pions de sa
		couleur sur le plateau.

	Mode d'affichage :
		Au vu de la grand part de personnes atteintes de Daltonisme dans la population,
		un mode spécifique a été ajouté avec un affichage plus adapté.

	Bonus :
		3 IA proposant des niveaux de difficulté différents sont proposés :
			[+] Facile
			[+] Normal
			[+] Difficile

		""")

	input("Press ENTER to return to the menu\n")

def daltonism_mode():
	pass

def create_initial_grid():
	"""Create the grid
	Create a grid of 8 x 8 with the corresponding coordinates
	contained into a tuple (x, y), the grid starts in top-left

	Args :
		None
	Return :
		return a list of dictionnaries containing coordinates and status of
	"""

	grid = {(x,y) : ' + ' for x in range(8) for y in range(8)}

	# Define initial positions 
	grid[(3,3)] = Data.current_mode[1][1]
	grid[(4,4)] = Data.current_mode[1][1]

	grid[(4,3)] = Data.current_mode[1][0]
	grid[(3,4)] = Data.current_mode[1][0]

	return grid


def create_player():
	"""Players attribution

	Ask to each player is pseudo and attribute him/her
	a role in the game

	Args : 
		None
	Return :
		return a dictionnary containing the pseudo and role
		of each players"""

	#TODO : Ajout d'une BDD des différents joueurs avec des scores et vérifier la présence des joueurs choisis dans cette BDD pour charger les scores

	# Default usernames if not defined by users
	activator, inhibitor = '', ''

	print("\nEntrez le pseudo du joueur",colors.GREEN + "'Activator' : " + colors.STOP, end = "")
	activator = input()

	print("\nEntrez le pseudo du joueur", colors.RED + "'Inhibitor' : "+colors.STOP, end = "")
	inhibitor = input()

	if len(activator) > 0:
		Data.current_player['Activator'] = activator
	if len(inhibitor) > 0:
		Data.current_player['Inhibitor'] = inhibitor


def display_grid(grid):
	"""Display grid

	Display the updated grid

	Args:
		grid : current grid to display
	Return:
		None"""

	s_activator, s_inhibitor = get_score(grid)

	print('\n     ',colors.GREEN + Data.current_player['Activator'] + colors.STOP, '   :', colors.BOLD + str(s_activator) + colors.STOP, 'points')
	print('\n     ',colors.RED + Data.current_player['Inhibitor'] + colors.STOP, '   :', colors.BOLD + str(s_inhibitor) + colors.STOP, 'points')

	print("""
            0     1     2     3     4     5     6     7
	 
            ▼     ▼     ▼     ▼     ▼     ▼     ▼     ▼   """, colors.BOLD + "(X)" + colors.STOP, end = '')

	print('\n\n')

	row = 0

	for i in range(8):
		print(' ', row, '  ▶ ', end = '   ')
		for j in range(8):
			print(grid[j,i], end = '   ')
		print('\n\n')
		row += 1

	print(colors.BOLD + ' (Y)\n' + colors.STOP)

def check_end(case, no_case, grid):
	"""Check end of the game

	Check if the game is finished. Verify that there are no more possibile moves
	signing the end of the game

	Args :
		grid : the actual grid
		case : the current player cases
		no_case : the opponent cases

	Return :
		return True if it is the end of the game, False in another way"""

	#TODO : Récupérer toutes les positions vides -> les tester avec le joueur courant ->si combinaison possible 
	# False sinon True et continue !

	free_cases = []
	for key, value in grid.items():
		if value == ' + ':
			free_cases.append(key)

	if len(free_cases) == 0:
		return True

	for elem in free_cases:
		status, useless = check_changes(elem, grid, case, no_case)
		if status == True:
			return False

	return True


def get_score(grid):
	"""Score function

	Get the current score for each player and return it as an integer
	Args :
		grid : the current grid
	Return :
		s_activator, s_inhibitor"""

	s_activator = 0
	s_inhibitor = 0

	for elem in grid.values():
		if elem == Data.current_mode[1][0]:
			s_activator += 1
		elif elem == Data.current_mode[1][1]:
			s_inhibitor += 1

	return s_activator, s_inhibitor


def check_changes(coordXY, grid, case = None, no_case = None):
	"""Check changes induced

	Check if the given coordinates induce changement of state
	into the grid. 

	Args :
		coordXY : tuple containing the coordinates (X,Y) chosen by the player
		grid : current grid
		case : value of the case of the current player
		no_case : value of the case of the non playing character

	Return :
		return True if the coordinates induce a changement else return False"""

	#TODO : Corriger -> erreur sur le droit de positionner les pions
	#	récupérer toutes les modifications possibles par le positionnement et les appliquer (pas le cas en ce moment)
	#	problème -> change état de tous les pions définis alentour et non pas uniquemet les bons. 

	#TODO : modifier l'orientation des positions -> vérifier présence no_case -> ajouter à tmp les pos jusque case.

	positions = get_allowed_positions(coordXY, grid)

	status = False
	taken_cases = []	

	for sublists in positions:
		tmp = []
		for elem in sublists:
			try:
				if grid[elem] == ' + ':
					break
				if grid[elem] == no_case:
					tmp.append(elem)
				if grid[elem] == case:
					taken_cases.extend(tmp)
					break
			except:
				pass

	if len(taken_cases) > 0:
		status = True
		
	return status, taken_cases

def update_grid(grid, taken_cases, case):
	"""Update the grid

	Update the current grid with the new position defined by the player,
	it modifies the grid to add the modification induced by the coordinates
	granted.

	Args :
		grid : the current grid w/o the modification
		taken_cases : spots taken by the player following his/her move
		case : symbol corresponding to the current player

	Return :
		None, modify the grid directly from the function"""

	# Modify the status of the taken spots
	for elem in taken_cases:
		for key in grid.keys():
			grid[elem] = case


def get_allowed_positions(coordXY, grid):
	"""Allowed positions

	Calculate the coordonates allowed for modifications

	Args :
		coordsXY : coordonates entered by the player
		grid : current grid
	Return :
		testing_coord : coordinates to test
		surrounging_coord : nearby coordinates of the coordXY spot"""

	surrounding_coord = []
	final_coord = []

	for i in range(-7, 8, 1):
		if (coordXY[0] + i, coordXY[1] + i) == coordXY:
			pass
		elif coordXY[0] + i not in range(8) or coordXY[1] + i not in range(8):
			surrounding_coord.append('None')
		else:
			surrounding_coord.append((coordXY[0] + i , coordXY[1] + i))

	for i in range(-7, 8, 1):
		if (coordXY[0] + i, coordXY[1] + i) == coordXY:
			pass
		elif coordXY[0] - i < 0 or coordXY[1] + i < 0 or coordXY[0] - i > 7 or coordXY[1] + i > 7:
			surrounding_coord.append('None')
		else:
			surrounding_coord.append((coordXY[0] - i, coordXY[1] + i))

	for i in range(-7, 8, 1):
		if (coordXY[0], coordXY[1] + i) == coordXY:
			pass
		elif coordXY[1] + i > 7 or coordXY[1] + i < 0:
			surrounding_coord.append('None')
		else:
			surrounding_coord.append((coordXY[0], coordXY[1] + i))

	for i in range(-7, 8, 1):
		if (coordXY[0] + i, coordXY[1]) == coordXY:
			pass
		elif coordXY[0] + i > 7 or coordXY[0] + i < 0:
			surrounding_coord.append('None')
		else:
			surrounding_coord.append((coordXY[0] + i, coordXY[1]))

	final_coord.append(surrounding_coord[:7][::-1])
	final_coord.append(surrounding_coord[7:14])
	final_coord.append(surrounding_coord[14:21][::-1])
	final_coord.append(surrounding_coord[21:28])
	final_coord.append(surrounding_coord[28:35][::-1])
	final_coord.append(surrounding_coord[35:42])
	final_coord.append(surrounding_coord[42:49][::-1])
	final_coord.append(surrounding_coord[49:])


	"""for elem in final_coord:
		print(elem)"""

	return final_coord

def get_position(c_player, case, no_case, grid):
	"""Get the position entered by the current player

	Get and check if the player give a position he can use. The player can not use a position
	if directly next to him there is not an occupied case. He can not use a position
	if the using of the position does not modify one protein at list. 

	Args :
		coordXY : the position the user submitted to place his protein
		case : the case associated with the current player
		grid : the current grid
	Return :
		coordXY : the coordinates chosen by the player"""

	#TODO : exception si joueur entre pas nombre

	stat = False

	# Player coordinates choice
	while not stat:

		display_grid(grid)

		try:
			print('\n' + c_player, 'a vous de jouer donnez la coordonnée de X : ', end = '')
			coordX = int(input())

			print('\n' + c_player, 'a vous de jouer donnez la coordonnée de Y : ', end = '')
			coordY = int(input())

			os.system('clear')

			if coordX not in range(8) or coordY not in range(8):
				raise ValueError

			if grid[coordX,coordY] != ' + ':
				raise ValueError

			stat, taken_cases = check_changes((coordX,coordY), grid, case, no_case)
			
			if stat == False:
				raise ValueError

			else:
				status = True

		except ValueError:
			print(""" 
 Vous ne respectez pas les conditions :

 	[+] Coordonnées dans l'intervalle 0 - 7

 	[+] Coordonnées devant induire le changement d'état d'au moins une protéine

 	[+] Coordonnées ne devant pas être celles d'une case déjà occupée
				""")

	return ((coordX,coordY), grid, taken_cases)


def playing(player, grid):
	"""Play a round

	Get the coordinates of the next case for the round

	Args :
		player : player of the current round
	Return :
		grid : the updated grid"""

	# ERROR : cases par défaut avec des valeurs de merde

	# Determine the current player and define the colors to use to fill the spots of the grid he chose
	if player == Data.current_player['Activator']:
		case = Data.current_mode[1][0]
		no_case = Data.current_mode[1][1]

	else:
		case = Data.current_mode[1][1]
		no_case = Data.current_mode[1][0]

	#end = check_end(case, no_case, grid)
	end = False
	if end == False:
		coordXY, grid, taken_cases = get_position(player, case, no_case, grid)

		# Modifies grid with the informations given by the player
		grid[coordXY] = case
		update_grid(grid, taken_cases, case)

	return grid, end

#################### Artificial Inteligence ####################

def easy_mode():
	pass

def hardcore_mode():
	pass