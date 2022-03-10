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

    return EstimatedRTT_list


def devRtt(sampleRtt: np.array, beta: float, estimatedRtt: list):


    Iteration_time = np.arange(0,len(sampleRtt))
    
    estimatedRtt = np.array(estimatedRtt)
    distance = np.abs(sampleRtt - estimatedRtt)

    devRtt_list = []
    devRtt_datapoint = distance[0]

    for i in range(0, len(sampleRtt)):

        devRtt_datapoint = (1-beta)*devRtt_datapoint + beta*distance[i]
        devRtt_list.append(devRtt_datapoint)


    fig = go.Figure()
    fig.add_trace(go.Scatter(x=Iteration_time, y=sampleRtt,
                    mode='lines+markers',
                    name='Sample RTT'))

    fig.add_trace(go.Scatter(x=Iteration_time, y=devRtt_list,
                    mode='lines+markers',
                    name='Estimated DevRTT'))
    fig.show()

    pass


def plot(option: int):

    print("Set alpha for EWMA routine (0<alpha<1)", end=" ")
    alpha = float(input())

    print("Set beta for devRtt routine (0<beta<1)", end=" ")
    beta = float(input())


    if option == 1:

        SampleRTT = []
        Iteration_time = []

        for i in range (0, 199):
            a = random.randint(150, 450)
            SampleRTT.append(a)
            Iteration_time.append(i)

        if option == 1:
            EWMA(SampleRTT, alpha, Iteration_time)
            #EWMA(ms, alpha, seg)

    if option == 2:

        #crea los datos en caso de que falten
        if 'data.csv' in listdir('./'):

            SampleRTT = pd.read_csv('./data.csv')
            npoints = SampleRTT.shape[0]
            Iteration_time = np.arange(0, npoints)

        else:

            npoints = int(input("¿cuantos datos quiere?"))
            create_random_points(npoints, 5)
            Iteration_time = np.arange(0, npoints)
            SampleRTT = pd.read_csv('./data.csv')

        estimated_rtt = EWMA(SampleRTT["# rtt"], alpha, Iteration_time)
        devRtt(SampleRTT["# rtt"], beta, estimated_rtt)
        #print(SampleRTT)
        #EWMA(ms, alpha, seg)

    


print("Select the input data option for EWMA routine")
print("1. Create 200 samples randomly")
print("2. Create n samples randomly (remove previous 'data.csv plz')")
opcion = int(input())

plot(opcion)
