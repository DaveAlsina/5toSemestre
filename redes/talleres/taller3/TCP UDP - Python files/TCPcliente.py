from socket import *

servidorNombre = "192.168.90.231" 
servidorPuerto = 12001
clienteSocket = socket(AF_INET, SOCK_STREAM)
clienteSocket.connect((servidorNombre,servidorPuerto))
mensaje = input("Ingrese un mensaje:")
clienteSocket.send(bytes(mensaje, "utf-8"))
mensajeRespuesta = clienteSocket.recv(1024)
print("Respuesta:\n" + str(mensajeRespuesta, "utf-8"))
clienteSocket.close()