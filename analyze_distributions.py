import numpy as np
import matplotlib.pyplot as plt

npfiles = np.load('data/dist3D.npz')

s = npfiles['arr_0']
dist_s = npfiles['arr_1']
t = npfiles['arr_2']
dist_t = npfiles['arr_3']

cut_s = np.less_equal(s, 50)
cut_t = np.less_equal(t, 50)

fit_param_s = np.polyfit(np.log(s[cut_s]), np.log(dist_s[cut_s]), 1)
fit_param_t = np.polyfit(np.log(t[cut_t]), np.log(dist_t[cut_t]), 1)

print fit_param_s
print fit_param_t

fit_s = np.exp(fit_param_s[0] * np.log(s) + fit_param_s[1])
fit_t = np.exp(fit_param_t[0] * np.log(t) + fit_param_t[1])

fig = plt.figure()
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

# Plot D(s)
ax1.scatter(s, dist_s, s = 40, c = 'k')
ax1.plot(s, fit_s, 'r-', lw = 3.0)
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.set_xlabel('s', size = 18)
ax1.set_ylabel('D(s)', size = 18)
ax1.tick_params(axis='both', which='major', labelsize=16)

# Plot D(t)
ax2.scatter(t, dist_t, s = 40, c = 'k', lw = 3.0)
ax2.plot(t, fit_t)
ax2.set_xscale('log')
ax2.set_yscale('log')
ax2.set_xlabel('T', size = 18)
ax2.set_ylabel('D(T)', size = 18)
ax2.tick_params(axis='both', which='major', labelsize=16)

plt.show()