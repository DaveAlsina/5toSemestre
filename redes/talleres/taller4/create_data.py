import numpy as np

def create_random_points(ncols, scaling):

    header = ['Rtt']
    data = np.random.rand(ncols, 1)*scaling
    np.savetxt('data.csv', (header + [d for d in data]), delimiter=',')

    pass







