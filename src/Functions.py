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

	grid = {(x,y) : ' + ' for x in range(8) for y in range(8)}

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


def check_changes(coordXY, case, no_case, grid):
	"""Check changes induced

	Check if the given coordinates induce changement of state
	into the grid. 

	Args :
		coordXY : tuple containing the coordinates (X,Y) chosen by the player

	Return :
		return True if the coordinates induce a changement else return False"""

	#TODO : Corriger -> erreur sur le droit de positionner les pions

	testing_coord, surrounding_coord = generate_allowed_positions(coordXY, grid)

	#print(surrounding_coord)
	#print(testing_coord)

	for key, value in testing_coord.items():
		for cle, valeur in surrounding_coord.items():

			if case in value and no_case in valeur and value != no_case:
				print('°°', key, '££', cle)
				grid[key] = case
				grid[cle] = case
				return grid, True
	
	return grid, False


"""
	for i in range(coordXY[0] - 2, coordXY[0] + 3, 4):
		for j in range(coordXY[1] - 2, coordXY[1] + 3, 2):
			try:
				if grid[i,j] == case and grid(i-1, j-1) not in [no_case, '   ']:
					print('T1')
					return True
			except KeyError:
				pass
	try:
		if grid[(coordXY[0], coordXY[1] - 2)] == case or grid[(coordXY[0], coordXY[1] + 2)] == case and grid[(coordXY[0], coordXY[1] - 1)] not in [no_case, '   '] or grid[(coordXY[0], coordXY[1] + 1)] not in [no_case, '   ']:
			print('T2')
			return True

		else:
			return False
	except:
		pass"""

def generate_allowed_positions(coordXY, grid):
	"""Allowed positions

	Calculate the coordonates allowed for modifications

	Args :
		coordsXY : coordonates entered by the player
		grid : current grid
	Return :
		testing_coord : coordinates to test
		surrounging_coord : nearby coordinates of the coordXY spot"""

	surrounding_coord = {}
	testing_coord = {}

	for i in range(coordXY[0] - 1, coordXY[0]+2, 1):
		for j in range(coordXY[1] - 1, coordXY[1] +2, 1):
			try:
				if i < 0 or j < 0:
					raise ValueError

				surrounding_coord[(i,j)] = grid[(i,j)]

			except ValueError:
				pass

			

	for i in range(coordXY[0] - 2, coordXY[0] + 3, 4):
		for j in range(coordXY[1] - 2, coordXY[1] + 3, 2):

			try:
				if i < 0 or j < 0 or i > 7 or j > 7:
					raise ValueError

				testing_coord[(i,j)] = grid[(i,j)]

			except ValueError:
				pass

	try:
		coord_tmp1 = (coordXY[0], coordXY[1] + 2)

		if coord_tmp1[1] not in range(8):
			raise ValueError

		testing_coord[(coordXY[0], coordXY[1] + 2)] = grid[(coordXY[0], coordXY[1] + 2)] 

		coord_tmp2 = (coordXY[0], coordXY[1] - 2)

		if coord_tmp2[1] not in range(8):
			raise ValueError

		testing_coord[(coordXY[0], coordXY[1] - 2)] = grid[(coordXY[0], coordXY[1] - 2)]

	except ValueError:
		pass

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

	status = False

	# Player coordinates choice
	while not status:
		#os.system('clear')

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

			grid, tmp = check_changes((coordX,coordY), case, no_case, grid)
			
			if tmp == False:
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

	return ((coordX,coordY), grid)


def playing(player, grid):
	"""Play a round

	Get the coordinates of the next case for the round

	Args :
		player : player of the current round
	Return :
		grid : the updated grid"""

	#TODO : Gestion des erreurs sur les coordonnées et sur les cases accessibles

	# Determine the current player and define the colors to use to fill the case of the grid he chose
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

	coordXY, grid = check_position(c_player, case, no_case, grid)

	# Modifies grid with the informations given by the player
	for key in grid.keys():
		if key == coordXY:
			grid[key] = case

	return grid
