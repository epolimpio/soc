import numpy as np
import matplotlib.pyplot as plt
import sandpile

nx = 50
ny = 50
grain_number = 100000

pile = sandpile.sandpile2D(nx, ny)
dist_t = dict()
dist_s = dict()

n_avalanche = 0

for grain in range(grain_number):
	
	if (pile.throw_sand() > pile.z_critical):
		n_avalanche += 1
		s, t = pile.avalanche()

		# Write distribution to histogram
		if s in dist_s:
			dist_s[s] += 1
		else:
			dist_s[s] = 1

		if t in dist_t:
			dist_t[t] += (1.0*s)/t
		else:
			dist_t[t] = (1.0*s)/t

	if 10*grain % grain_number == 0:
		print str(100*grain/grain_number) + '%'

np.savez('data/distribution.npz', np.array(dist_s.keys()), (1.0*np.array(dist_s.values()))/n_avalanche,
	np.array(dist_t.keys()), np.array(dist_t.values())/n_avalanche)

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

ax1.plot(np.array(dist_s.keys()), (1.0*np.array(dist_s.values()))/n_avalanche)
ax2.plot(np.array(dist_t.keys()), np.array(dist_t.values())/n_avalanche)

ax1.set_xscale('log')
ax1.set_yscale('log')
ax2.set_xscale('log')
ax2.set_yscale('log')

plt.show()


