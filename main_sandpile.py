import numpy as np
import matplotlib.pyplot as plt
import sandpile

nx = 5
ny = 5
grain_number = 1000

pile = sandpile.sandpile2D(nx, ny)
plt.ion()

for grain in range(grain_number):
	
	if (pile.throw_sand() > pile.z_critical):
		pile.avalanche()

	plt.clf()
	cplt = plt.contourf(np.arange(nx), np.arange(ny), pile.z)
	bar = plt.colorbar(cplt, orientation = 'vertical')
	plt.draw()



