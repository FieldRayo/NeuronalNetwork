from NN import *
import random

"""
This code is a data generator that will be received by the perceptron
for training with the inputted data.
"""

# DataSets
def dataset1(data_size, limit):
    x, y = [], []
    
    for i in range(data_size):
        x.append([(random.randint(1, limit)) for i in range(2)])
    
    for i in x:
        if i[0] + i[-1] >= limit:
            y.append(1)
        else:
            y.append(0)
            
    return x, y
    
data_size = 2000
limit = 12
    
x, y = dataset1(data_size, limit)    
    
NN = NeuronalNetwork(x, y, epoch=1000, act_func=umbral, n_weights=2)
NN.attemp()
