# -*- coding: utf-8 -*-

from . import Data

# Add colors into the terminal
class colors:
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

	grid = [{(x,y) : ' + ' } for y in range(8) for x in range(8)]

	grid[27][(3,3)] = colors.REDB + "   " + colors.STOP
	grid[28][(4,3)] = colors.GREENB + "   " + colors.STOP
	grid[35][(3,4)] = colors.GREENB + "   " + colors.STOP
	grid[36][(4,4)] = colors.REDB + "   " + colors.STOP

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

	print("Entrez le pseudo du joueur",colors.GREEN + "'Activator' : " + colors.STOP, end = "")
	activator = input()

	print("Entrez le pseudo du joueur", colors.RED + "'Inhibitor' : "+colors.STOP, end = "")
	inhibitor = input()

	if len(activator) == 0:
		activator = 'Activator'

	if len(inhibitor) == 0:
		inhibitor = 'Inhibitor'

	Data.current_player['Activator'] = activator
	Data.current_player['Inhibitor'] = inhibitor


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

	row = 0

	for i in range(64):
		for value in grid[i].values():
			if i % 8 == 0:
				print('\n\n\n  ' + str(row) + '   ▶   ' , str(value), end = '   ')
				row += 1

			else:
				print(str(value), end = '   ')
	print(colors.BOLD + '\n\n (Y)' + colors.STOP)


	print('\n')

def playing(player, grid):
	"""Play a round

	Get the coordinates of the next case for the round

	Args :
		player : player of the current round
	Return :
		coordinates : coordinates of the chosen case as a tuple (X,Y)"""

	#TODO : Gestion des erreurs sur les coordonnées et sur les cases accessibles

	if player == Data.current_player['Activator']:
		case = colors.GREENB + '   ' + colors.STOP

	else:
		case = colors.REDB + '   ' + colors.STOP

	print(player, 'a vous de jouer donnez la coordonnée de X : ', end = '')
	coordX = int(input())

	print(player, 'a vous de jouer donnez la coordonnée de Y : ', end = '')
	coordY = int(input())

	coordXY = (coordX,coordY)

	for i in range(len(grid)):
		for key in grid[i].keys():
			if key == coordXY:
				grid[i][coordXY] = case

	return grid

