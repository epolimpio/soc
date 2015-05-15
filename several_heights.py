import numpy as np
import matplotlib.pyplot as plt

ns = [20, 30, 50, 60]
cs = 'krbg'
calc = 0

fig1 = plt.figure()
ax1 = fig1.add_subplot(1,1,1)
fig2 = plt.figure()
ax2 = fig2.add_subplot(1,1,1)
f_av = []

for n, c in zip(ns, cs):
	filename = 'data/distheight_' + str(n) + str(n) + str(calc) + '.npz'
	npfiles = np.load(filename)

	nu = 0.93
	beta = 1.86
	sands_out = npfiles['arr_4']
	dist_sands_out = npfiles['arr_5']

	c_str = c + 'o'
	ax1.plot(sands_out, dist_sands_out, c_str, label = 'N = ' + str(n))
	ax1.set_xscale('log')
	ax1.set_yscale('log')
	ax1.set_xlabel('d', size = 24)
	ax1.set_ylabel('D(d)', size = 24)
	ax1.tick_params(axis='both', which='major', labelsize=20)
	ax1.legend()

	ax2.plot(sands_out/(n**nu), (n**beta)*dist_sands_out, c_str, label = 'N = ' + str(n))
	ax2.set_xscale('log')
	ax2.set_yscale('log')
	ax2.set_xlabel(r'$d/L^{'+str(nu)+'}$', size = 24)
	ax2.set_ylabel(r'$D(d)L^{'+str(beta)+'}$', size = 24)
	ax2.tick_params(axis='both', which='major', labelsize=20)
	ax2.legend()

plt.show()