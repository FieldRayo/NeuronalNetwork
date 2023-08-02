from sklearn.datasets import *
import matplotlib.pyplot as plt
import numpy as np
import ast


def get_datasets(data_s, size, type_dataset):
    make_datasets = {"make_circles": make_circles(size, noise=0.05), "make_moons": make_moons(size, noise=0.05),
                     "fried_man": make_friedman1(size, noise=0.05), "make_classification": make_classification(size),
                     "make_blobs": make_blobs(size), "make_hastie_10_2": make_hastie_10_2(size)}
    
    load_datasets = {"wine": load_wine(), "breast_cancer": load_breast_cancer(),
                     "iris": load_iris(), "diabetes": load_diabetes(),
                     "digits": load_digits()}
    
    personalized_datasets = {}
    
    inputs, target = 0, 0
    
    if type_dataset == 0:
        inputs, target = make_datasets[data_s]
    elif type_dataset == 1:
        all_data = load_datasets[data_s]
        inputs, target = (all_data["data"], all_data["target"])
    elif type_dataset == 2:
        inputs, target = personalized_datasets[data_s]
    elif type_dataset == 3:
        inputs = ast.literal_eval(input("- set inputs, example: [[1, 2], [3, 4]] -\n>>> "))
        target = ast.literal_eval(input("- set target, example: [1, 0] -\n>>> "))
        
        inputs = np.array(inputs)
        target = np.array(target)
        
        personalized_datasets[f"{data_s}"] = inputs, target
    else:
        return "¡set a correct data type!(0, 1, 2, 3)"
    
    if len(target.shape) == 1:
        target = target.reshape(target.shape[0], 1)
    
    return inputs, target


# x, y = get_datasets("test", 100, 3)
# plt.scatter(x[:, 0], x[:, 1], c=y)
# plt.show()
