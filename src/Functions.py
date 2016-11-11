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

	print("Entrez le pseudo du joueur",colors.GREEN + "'Activator' : " + colors.STOP, end = "")
	activator = input()

	print("Entrez le pseudo du joueur", colors.RED + "'Inhibitor' : "+colors.STOP, end = "")
	inhibitor = input()

	if len(activator) == 0:
		activator = 'Activator'

	if len(inhibitor) == 0:
		inhibitor = 'Inhibitor'

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
	 
            ▼     ▼     ▼     ▼     ▼     ▼     ▼     ▼   """, colors.BOLD + "(X)" + colors.STOP)

	row = 0

	for i in range(64):
		for value in grid[i].values():
			if i % 8 == 0:
				print('  \n  \n  ' + str(row) + '   ▶   ' , str(value), end = '   ')
				row += 1

			else:
				print(str(value), end = '   ')
	print(colors.BOLD + '\n\n (Y)' + colors.STOP)


	print('\n')

def playing():
	pass