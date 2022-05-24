# Redes de Computadores 2022
# Universidad del Rosario - School of Engineering, Science and Technology
# Pr. David Celeita
from Proyecto_Final_Redes import *
import cv2
from  scipy.sparse import csr_matrix

# This is 0 main function. The interaction between user and tool si performed here.

print("\n Welcome to Link-State routing Tool based on Dijkstra!")

selection = input("Select 0 if you want me to create a random graph for you. Press 1 if you want to upload it \n Type your selection and press enter: ")


if selection == '0':
    is_valid = False
    while is_valid != True:
        num_nodes = int(input("Choose the number of nodes in the graph. They must be between 15 and 50: "))
        if 15 <= num_nodes and num_nodes <= 50:
            is_valid = True

    rand_sparse = create_random_sparse(num_nodes) 
    graph = Graph(rand_sparse)
    G = graph.draw_graph()
    G2 = graph.dijkstra()

    print(type(G))
    print(type(G2))
    img = nx.adjacency_matrix(G, weight = 'weight')
    print("matriz de adyacencia sin ser ndarray")
    print(img)

    img = csr_matrix.todense(img)
    print("matriz en versión densa")
    print(img)

    print(img.shape)
    
    cv2.imshow("loca", img)

else:
    is_valid = False
    while is_valid != True:
        doc_type = str(input("If you want to upload a CSV file type CSV or if you want a TXT file type TXT. \n Type your selection and press enter: "))
        if doc_type == "CSV" or doc_type == "TXT":
            is_valid = True
    
    filename = input("\n Now, type the name of the file. Remember that it must be in the same folder of this .exe or specify the whole path. \n Type you filename with the extension: ")
    
    if doc_type == "CSV":
        sparse_m = import_csv(filename)
        graph = Graph(sparse_m)
        graph.draw_graph()
        graph.dijkstra()

    else:
        sparse_m = import_txt(filename)
        graph = Graph(sparse_m)
        graph.draw_graph()
        graph.dijkstra()






