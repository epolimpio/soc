#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sandpile

nx = 50
ny = 50
grain_number = 50000

pile = sandpile.sandpile2D(nx, ny, movie = False)

fig0 = plt.figure()
ax0 = fig0.add_subplot(1,1,1)

for grain in range(grain_number):
	
	if (pile.throw_sand() > pile.sigma_critical):
		pile.avalanche()
		if np.sum(pile.last_cluster) > 100:
			break


ax0.clear()
cplt0 = plt.imshow(pile.last_cluster.astype(int),  cmap='Greys', interpolation = 'none')
plt.show()
