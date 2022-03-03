# EstimatedRTT Routine
# This script allows the user to create a random set of 200 samples (between 150 and 450 ms).
# Then, the user can select the value of Alpha to reproduce the estimatedRTT
# Part of the course - Computed Networks by Pr. David Celeita (david.celeita@urosario.edu.co)

import csv, random, os
import plotly.graph_objects as go
from os import listdir
from create_data import *
import pandas as pd

def EWMA(SampleRTT, alpha, Iteration_time):
    fig = go.Figure()
    EstimatedRTT_list = []

    EstimatedRTT = SampleRTT[0]
    for i in range(0, len(SampleRTT)):
        EstimatedRTT  = ((1- alpha) * EstimatedRTT) + (alpha*SampleRTT[i])
        EstimatedRTT_list.append(EstimatedRTT)

    fig.add_trace(go.Scatter(x=Iteration_time, y=SampleRTT,
                    mode='lines+markers',
                    name='Sample RTT'))

    fig.add_trace(go.Scatter(x=Iteration_time, y=EstimatedRTT_list,
                    mode='lines+markers',
                    name='Estimated RTT'))
    fig.show()

def plot(option: int):

    print("Set alpha for EWMA routine (0<alpha<1)", end=" ")
    alpha = float(input())

    if option == 1:

        SampleRTT = []
        Iteration_time = []

        for i in range (0, 199):
            a = random.randint(150, 450)
            SampleRTT.append(a)
            Iteration_time.append(i)

        if option == 1:
            EWMA(SampleRTT, alpha, Iteration_time)
            EWMA(ms, alpha, seg)

    if option == 2:

        print(not('data.csv' in listdir('./')))

        if not ('data.csv' in listdir('./')):

            create_random_points(5000, 5)
            Iteration_time = np.arange(0, 5000)
            SampleRTT = pd.read_csv('./data.csv')

            print(SampleRTT)

    


print("Select the input data option for EWMA routine")
print("1. Create 200 samples randomly")
opcion = int(input())

plot(opcion)
