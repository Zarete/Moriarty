# -*- coding: utf-8 -*-

from . import Data
import os

# Add colors into the terminal
class colors:
	
	HEADER = '\033[95m'

	GREENB = '\033[42m'
	GREEN = '\033[92m'

	REDB = '\033[41m'
	RED = '\033[91m'

	STOP = '\033[0m'
	BOLD = '\033[1m'


def create_initial_grid():
	"""Create the grid

	Create a grid of 8 x 8 with the corresponding coordinates
	contained into a tuple (x, y), the grid starts in top-left

	Args :
		None
	Return :
		return a list of dictionnaries containing coordinates and status of
	"""

	grid = {(x, y) : ' + ' for x in range(8) for y in range(8)}

	# Define initial positions 
	grid[(3,3)] = colors.REDB + "   " + colors.STOP
	grid[(4,3)] = colors.GREENB + "   " + colors.STOP
	grid[(3,4)] = colors.GREENB + "   " + colors.STOP
	grid[(4,4)] = colors.REDB + "   " + colors.STOP

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

	activator = ''
	inhibitor = ''

	print("\nEntrez le pseudo du joueur",colors.GREEN + "'Activator' : " + colors.STOP, end = "")
	activator = input()

	print("\nEntrez le pseudo du joueur", colors.RED + "'Inhibitor' : "+colors.STOP, end = "")
	inhibitor = input()

	# Default usernames if not defined by users
	if len(activator) == 0:
		activator = 'Activator'

	if len(inhibitor) == 0:
		inhibitor = 'Inhibitor'

	# Attribute to each player the status he chose
	Data.current_player['Activator'] = activator
	Data.current_player['Inhibitor'] = inhibitor

	return activator, inhibitor


def display_grid(grid):
	"""Display grid

	Display the updated grid

	Args:
		grid : current grid to display
	Return:
		None"""

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
		status, useless2 = check_changes(elem, grid, case, no_case)
		if status == True:
			return False

	return True


	print(occupied_cases)
	print(free_cases)



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

	testing_coord, surrounding_coord = get_allowed_positions(coordXY, grid)

	status = False
	taken_cases = []

	# Check if the position given modifies one spot at list
	for i in range(len(testing_coord)):
		try:
			if grid[testing_coord[i]] == case and grid[surrounding_coord[i]] == no_case:
				taken_cases.append(surrounding_coord[i])
				status = True

		except KeyError:
			pass

	return status, taken_cases


def update_grid(grid, taken_cases, case):
	"""Lol"""

	# Modify the colors of the taken spots
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
	testing_coord = []

	# Get the coordinates of the external square
	for i in range(coordXY[0] - 1, coordXY[0] + 2, 2):
		for j in range(coordXY[1] - 1, coordXY[1] +2, 1):
			if (i,j) == coordXY:
				pass
			elif i < 0 or j < 0:
				surrounding_coord.append('None')
			else:
				surrounding_coord.append((i,j))

	# Get the coordinates of the internal square
	for i in range(coordXY[0] - 2, coordXY[0] + 3, 4):
		for j in range(coordXY[1] - 2, coordXY[1] + 3, 2):
			if i < 0 or j < 0 or i > 7 or j > 7:
				testing_coord.append('None')
			else:
				testing_coord.append((i,j))

	# Get the position of Bottom and Top of the 2 squares
	TC = [(coordXY[0], coordXY[1] + 2), (coordXY[0], coordXY[1] - 2)]
	for elem in TC:

		if elem[0] not in range(8) or elem[1] not in range(8):
			testing_coord.append('None')
		else:
			testing_coord.append(elem)


	SC = [(coordXY[0], coordXY[1] + 1), (coordXY[0], coordXY[1] - 1)]
	for elem in SC:
		if elem[0] not in range(8) or elem[1] not in range(8):
			surrounding_coord.append('None')
		else:
			surrounding_coord.append(elem)

	return testing_coord, surrounding_coord

def check_position(c_player, case, no_case, grid):
	"""Check given position

	Check if the player give a position he can use. The player can not use a position
	if directly next to him there is not an occupied case. He can not use a position
	if the using of the position does not modify one protein at list. 

	Args :
		coordXY : the position the user submitted to place his protein
		case : the case associated with the current player
		grid : the current grid
	Return :
		coordXY : the coordinates chosen by the player"""

	stat = False

	# Player coordinates choice
	while not stat:

		try:
			print('\n' + c_player, 'a vous de jouer donnez la coordonnée de X : ', end = '')
			coordX = int(input())

			print('\n' + c_player, 'a vous de jouer donnez la coordonnée de Y : ', end = '')
			coordY = int(input())

			if coordX not in range(8) or coordY not in range(8):
				print('E1')
				raise ValueError

			if grid[coordX,coordY] != ' + ':
				print('E2')
				raise ValueError

			stat, taken_cases = check_changes((coordX,coordY), grid, case, no_case)
			
			if stat == False:
				print('E3')
				raise ValueError

			else:
				status = True

		except ValueError:
			print(""" 
 Vous ne respectez pas les conditions :

 	[+] Coordonnées dans l'intervalle 0 - 7

 	[+] Coordonnées doivent induire un changement d'état d'au moins une protéine

 	[+] Coordonnées ne doivent pas être celles d'une case déjà modifiée
				""")

	return ((coordX,coordY), grid, taken_cases)


def playing(player, grid):
	"""Play a round

	Get the coordinates of the next case for the round

	Args :
		player : player of the current round
	Return :
		grid : the updated grid"""

	# Determine the current player and define the colors to use to fill the spots of the grid he chose
	if player == Data.current_player['Activator']:
		case = colors.GREENB + '   ' + colors.STOP
		no_case = colors.REDB + '   ' + colors.STOP
		c_player = colors.GREEN + player + colors.STOP
		print('Joueur actuel : ' + colors.GREEN + player + colors.STOP)

	else:
		case = colors.REDB + '   ' + colors.STOP
		no_case = colors.GREENB + '   ' + colors.STOP
		c_player = colors.RED + player + colors.STOP
		print('Joueur actuel : ' + colors.RED + player + colors.STOP)

	end = check_end(case, no_case, grid)

	if end == False:
		coordXY, grid, taken_cases = check_position(c_player, case, no_case, grid)

		# Modifies grid with the informations given by the player
		grid[coordXY] = case
		update_grid(grid, taken_cases, case)

	return grid, end

if __name__ == "__main__":

	end = check_end()
	print("ENDING :", end)