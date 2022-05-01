import numpy as np 
import matplotlib.pyplot as plt
import random
plt.rc('text', usetex=True)

start = 0
end = 8

time = np.arange(1,100, 0.1)
a = 2
w = 3
d = 2

nrows = 4
ncols = 2
fig, axes = plt.subplots(nrows, ncols)#, dpi = 300)
fig.tight_layout(pad=1)

factors_dict = {}

for k in range(0, end ):

    factor = random.randint(0, 20)

    while factor in factors_dict.keys():
        factor = random.randint(2, 20)

    factors_dict[factor] = 0

    i = a*np.cos(time*w + d)
    j = a*np.cos(time*w*factor + d)

    #row = max( (k//ncols) - 1, 0)
    #col = max( (k%ncols) - 1, 0)
    row = k//ncols
    col = k%ncols 

    print(k, ncols)
    print(row, col)
    print()
    axes[row, col].plot(i,j)
    axes[row, col].set_title("$\omega_1 = {}$ , $\omega_2 ={}$".format(w, w*factor))

plt.show()
# Make room for the ridiculously large title.
plt.subplots_adjust(top=0.8)


