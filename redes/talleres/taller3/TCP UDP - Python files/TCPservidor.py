from socket import *
from os import listdir

servidorPuerto = 12005
servidorSocket = socket(AF_INET,SOCK_STREAM)
servidorSocket.bind(('',servidorPuerto))
servidorSocket.listen(1)


print("El servidor está listo para recibir mensajes")
while 1:
    conexionSocket, clienteDireccion = servidorSocket.accept()
    print("Conexión establecida con ", clienteDireccion)
    mensaje = str( conexionSocket.recv(1024), "utf-8" )

    files = listdir("./files")
    print(files)

    print("Mensaje recibido de ", clienteDireccion)
    print(mensaje)

    if mensaje in files:

        fileObject = open("./files/"+ mensaje, "r")
        mensajeRespuesta = fileObject.read()
        print(mensajeRespuesta)


    else: 

        mensajeRespuesta = "ERROR 404"

    conexionSocket.send(bytes(mensajeRespuesta, "utf-8"))
    conexionSocket.close()



