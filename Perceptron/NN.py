"""
This neural network takes two numbers as input,
and if the sum of the two numbers is greater than or equal to 10,
it returns 1, otherwise it returns 0.
This is my first functional neural network, so it's very basic.

You can configure its training data in TestNN.py.

is "It can be executed in TestNN.py with the default data already set.
"""

import numpy as np
import matplotlib.pyplot as plt

umbral = lambda x, b: 1 if x + b >= 0 else 0
sigmoid = lambda x, b: 1 / (1 + np.e ** -(x+b))
relu = lambda x, b: max(0,x+b)

"""
input = [Years_old, Money]
output = platinum_card_access: 1 = True, 0 = False

x = [[0.5, 0.6], [0.4, 0.7], [0.3, 0.8],  # 1
     [0.1, 0.2], [0.3, 0.4],  # 0
     [0.6, 0.5], [0.7, 0.4], [0.8, 0.3],  # 1
     [0.2, 0.1], [0.4, 0.3]]  # 0

y = [1, 1, 1,
     0, 0,
     1, 1, 1,
     0, 0]
"""


class NeuronalNetwork:
    def __init__(self, x, y, epoch=1000, act_func=umbral, n_weights=2):
        # Hidden Layer
        self.x = x
        self.y = y
        self.w = np.random.uniform(-1, 1, size=n_weights)
        self.b = np.random.uniform(-1, 1)
        
        self.act_func = act_func
        self.epoch = epoch

        # Start
        self.main(self.x, self.y, self.w, self.b, self.act_func)

        # Save
        self.save()

    def main(self, x, y, w, b, act_func):
        epoch = self.epoch
        outs = []

        for i in range(epoch):
            # Start Hidden Layer
            sigma = self.sigma(x, w)
            outs = [act_func(i, b) for i in sigma]
            cost = [(j - i) for i, j in zip(outs, y)]
            # Training
            w, b = self.ajust(cost, w, x, b)
            # Bar progress
            self.progress(epoch, i)
        # Set data train
        self.w, self.b = w, b
        # View correct persentage
        self.percentage(outs, y)
        
    def sigma(self, x, W):
        sigmas = []
        
        for i in x:
            sigmas.append(sum([j * w for j, w in zip(i, W)]))

        return sigmas

    def ajust(self, cost, W, X, b):
        lerning_rate = 0.01
        len_x, len_w = len(X), len(W)

        for nx, x in enumerate(X):
            for n in range(len_w):
                W[n] += lerning_rate * x[len_x % 2] * cost[nx]
                b += lerning_rate * cost[nx]

        return W, b

    def attemp(self):
        while True:
            xs = (input("\n>>> ")).split()

            if xs[-1] == "W":
                print(self.w, self.b)
                continue
            
            if xs[0] == "DATA":
                pen = int(xs[-1])
                sigma = self.sigma(self.x, self.w)
                outs = [self.act_func(i, self.b) for i in sigma]
                print(f"\nInputs: {self.x[:pen]}\nOutputs: {self.y[:pen]}")
                continue
            
            if xs[-1].isalpha():
                break
            try:
                xs = [float(x) for x in xs]
                sigma = self.sigma([xs], self.w)
                print(self.act_func(sigma[0], self.b))
            except:
                print(f'Syntax Error: "{xs}"')
                continue

    def progress(self, times, i):
        progress = round(100 / (times / (i + 1)))
        bar = '#' * (progress // 10) + '-' * (10 - progress // 10)
        print(f"\rLoading Training: {progress}% [{bar}]", end="")

    def save(self):
        f = open("train.txt", "w+")
        f.seek(0, 2)  # mueve el puntero de archivo al final del archivo
        f.write(f"{self.w}\n")
        f.close()

    def percentage(self, out, y):
        n = len([i for i, j in zip(out, y) if round(i) == j])
        print(f"\n\nCorrect: {100 / (len(out) / n)}%")
