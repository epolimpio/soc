#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import avalanche

nx = 10
ny = 10
grain_number = 1000
critical_slope = 4

pile = avalanche.avalanche2D(nx, ny)

for grain in range(grain_number):
	
	if (pile.throw_sand() > critical_slope):
		pile.avalanche()

