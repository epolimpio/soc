#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sandpile

nx = 50
ny = 50
grain_number = nx*ny*10

pile = sandpile.sandpile2D(nx, ny, movie = True)

for grain in range(grain_number):
	
	if (pile.throw_sand() > pile.sigma_critical):
		pile.avalanche()
