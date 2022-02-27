import numpy as np
import matplotlib.pyplot as plt
interval = 0.01

# Constantes
t_0 = 0
t_f = 10
G = 4*np.pi**2
M = 1.0
m = 5
v_0x = 0
v_0y = 4
x_0 = 1
y_0 = 0

#Ro  = 1 # Radio d ela orbita 
#v =np.sqrt(G*M/Ro) # v asumiendo orbita circular
t = 0 # tiempo ini
tf = 10
v_x = [v_0x]
v_y = [v_0y]
x_n = [x_0]
y_n = [y_0]
t_n = [t_0]
vx  = v_0x
vy  = v_0y
x_new   = x_0
y_new   = y_0
t   = t_0



while t < tf:
	x = x_new + vx*interval       # Se implementa Euler
	y = y_new + vy*interval
	r = np.sqrt(x**2 + y**2)
	vx = vx - interval *(G*M*x)/r**3 # aqui esta la aceleracion
	vy = vy - interval *(G*M*y)/r**3
	x_n = np.append(x_n,x)   # ADICIONA NUEVOS PUNTOS AL ARREGLO
	y_n = np.append(y_n,y)
	v_x =np.append(v_x,vx)
	v_y = np.append(v_y,vy)
	t_n = np.append(t_n,t)
	x_new = x    # ACTUALIZA X
	y_new = y
	t = t + interval # INCREMENTA EL TIEMPO
 

plt.plot(x_n, y_n)
plt.show()

