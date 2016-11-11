# -*- coding: utf-8 -*-


# Add colors into the terminal
class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    GREEN = '\033[92m'
    xxx = '\033[93m'
    RED = '\033[91m'
    STOP = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def player_definition():
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

	activator = input(colors.GREEN+"Entrez le pseudo du joueur 'Activator' : "+colors.STOP)
	inhibitor = input(colors.RED+"Entrez le pseudo du joueur 'Inhibitor' : "+colors.STOP)

	return activator, inhibitor


def display_grid(grid):
	"""Display grid

	Display the updated grid

	Args:
		grid : current grid to display
	Return:
		None"""

	for i in range(64):
		for value in grid[i].values():
			if i % 8 == 0:
				print('\n\n' + str(value), end = ' ')

			else:
				print(str(value), end = ' ')

	print('\n')

def playing():
	pass