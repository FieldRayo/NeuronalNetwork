from sklearn.datasets import make_circles

inputs, target = make_circles(500, factor=0.1, noise=0.07)
target = target.reshape(500, 1)
