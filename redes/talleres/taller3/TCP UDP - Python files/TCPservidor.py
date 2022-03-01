from socket import *
from os import listdir

servidorPuerto = 12005
servidorSocket = socket(AF_INET,SOCK_STREAM)
servidorSocket.bind(('',servidorPuerto))
servidorSocket.listen(1)


print("El servidor está listo para recibir mensajes")

conexionSocket, clienteDireccion = 0, 0 
files = ["Foto1", "Foto2", "Foto3"]
print(files)

while clienteDireccion == 0:

    conexionSocket, clienteDireccion = servidorSocket.accept()
    print("Conexión establecida con ", clienteDireccion)

# lista de mensajes solicitud del cliente
new_messages = ['']

while 1:

    mensaje = str( conexionSocket.recv(1024), "utf-8" )

    print("Mensaje recibido de ", clienteDireccion)
    print(mensaje)


    if mensaje == 'FOTOS':

        mensajeRespuesta = ",".join(files)
        conexionSocket.send(bytes(mensajeRespuesta, "utf-8"))
        
        local_message = ""

        while local_message == '':
            local_message = str( conexionSocket.recv(1024), "utf-8" )
            print("esperando...")


        new_messages.append( local_message ) 

        print("Mensaje recibido de ", clienteDireccion)
        print(local_message)

        if  (new_messages[-1] in ['1', '2', '3']) and (new_messages[-1] != new_messages[-2]):
            conexionSocket.send(bytes('ACK', "utf-8"))
                
        elif (new_messages[-1] not in ['1', '2', '3']):
            
            conexionSocket.send(bytes('ERROR 404', "utf-8"))

        else:
            conexionSocket.send(bytes('304', "utf-8"))

    else: 

        mensajeRespuesta = "ERROR 404"
        conexionSocket.send(bytes(mensajeRespuesta, "utf-8"))

    if mensaje == 'EXIT':
        conexionSocket.close()



