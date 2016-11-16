# -*- coding: utf-8 -*-

from . import Functions as Functions

user = [{'pseudo' : 0}]

current_player = {'Activator' : Functions.colors.GREEN+'Activator'+Functions.colors.STOP, 'Inhibitor' : Functions.colors.RED+'Inhibitor'+Functions.colors.STOP}

mode = [['(Daltonien)', [Functions.colors.GREEN+'[A]'+Functions.colors.STOP, Functions.colors.RED+'[I]'+Functions.colors.STOP]],
	    ['(Normal)   ', [Functions.colors.GREENB+'   '+Functions.colors.STOP, Functions.colors.REDB+'   '+Functions.colors.STOP]]]

current_mode = mode[1]
