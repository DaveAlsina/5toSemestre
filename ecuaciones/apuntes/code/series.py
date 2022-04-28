import numpy as np 
import matplotlib.pyplot as plt
import sys

print("El N escogido es: ", sys.argv[1]) # prints var1
N = int(sys.argv[1])

print("El intervalo va desde -{}pi hasta {}pi".format(sys.argv[2],sys.argv[2]) )
interval_lenght = float(sys.argv[2])


def b_n(n: int):

    return 2 * (np.power(-1, n)/ (np.pi * n))


#intervalo de la función
interval = (-interval_lenght*np.pi, interval_lenght*np.pi)

#vector de theta
theta = np.arange(start = interval[0], stop = interval[1], step = 0.1)


#iteracion 1
function = np.sin( (1 * np.pi)*theta) * b_n(1)

#resto de iteraciones
for n in range(2, N):
    
    function += np.sin( (n * np.pi)*theta) * b_n(n)


plt.plot(function)
plt.show()


