import numpy as np

def create_random_points(ncols, scaling):

    data = np.random.rand(ncols, 1)*scaling
    np.savetxt('data.csv',  data, delimiter=',', header = 'rtt' )

    pass


#create_random_points(100, 3)




