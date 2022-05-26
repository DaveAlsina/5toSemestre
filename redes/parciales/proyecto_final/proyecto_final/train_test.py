import numpy as np
from matplotlib import pyplot as plt


from os import getcwd, listdir
import re

# busca la ruta actual para crear el directorio en caso
# de que no exista
cwd = getcwd()
data_dir = cwd + '/data'

def train_test_split(train = 0.8, test = 0.2):

    """

        OUTPUT:
                (train_input, train_output,  test_input, test_output), 

                train.shape = (80% * ndata, 100, 100, 1)
                test.shape  = (20% * ndata, 100, 100, 1)
    """

    input_data, output_data = get_dataset()

    # obtiene los nombres de los archivos
    in_files,  _  = input_data
    out_files, _  = output_data

    # obtiene los nombres de los archivos
    ntrain = int(np.floor(input_data[1] * train))
    ntest  = int(np.ceil(output_data[1]  * test))

    files_path =  data_dir + '/'

    # carga los datos 
    img = np.load(files_path + in_files[0])
    data_shape = img.shape

    print(data_shape, ntrain)
    plt.imshow(img)
    plt.show()
    
    train_input = np.zeros( (ntrain, data_shape[0], data_shape[1]) )

    # carga los datos de entrenamiento
    count = 0 
    for i in in_files[:ntrain]:


        train_input[count] = np.load(files_path + i)
        plt.imshow(train_input[count])
        plt.show()

        count += 1

    print(train_input)


def get_dataset():

    data   = listdir(data_dir)
    data   = ', '.join(data) 

    input_pattern = 'input_\d+.npy'
    output_pattern = 'output_dijkstra_\d+.npy'


    # obtiene los nombres de los archivos input
    inputs  = re.findall(input_pattern, data)

    # obtiene los nombres de los archivos output
    outputs = re.findall(output_pattern, data)
    
    return (inputs, len(inputs)), (outputs, len(outputs))


train_test_split()










