#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import avalanche

nx = 10
ny = 10
grain_number = 1000

pile = avalanche.avalanche2D(nx, ny)

sands_out = 0
for grain in range(grain_number):

	height, slope = pile.throw_sand()
	
	if (height > pile.sigma_critical):
		pile.avalanche()

