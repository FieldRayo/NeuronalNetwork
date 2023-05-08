<div align="center">
  <h1><img src="neural-network.png" alt="Neural Network" width="400px"></h1>
</div>

---

<p align="justify">
    <img src="divider.png" alt="Divider" width="100%">
</p>

<div align="center">
    <h2>Neural Network Code Description</h2>
</div>

<p align="center">
    <img src="divider.png" alt="Divider" width="70%">
</p>

<p align="justify">
    This code represents a simple neural network that takes two numbers as input and returns 1 if the sum of the two numbers is greater than or equal to 10; otherwise, it returns 0. The neural network is designed with a single hidden layer.
</p>

<p align="justify">
    The neural network code is imported from the `NN.py` module using the statement `from NN import *`. This module contains the implementation of the `NeuronalNetwork` class and other necessary functions.
</p>

<p align="justify">
    Additionally, there is a data generator function, `dataset1`, defined in the code. This function generates a dataset of random input-output pairs based on the specified `data_size` and `limit`. The inputs (`x`) are randomly generated pairs of numbers between 1 and the given `limit`. The outputs (`y`) are calculated based on whether the sum of each input pair is greater than or equal to the `limit`. If it is, the output is 1; otherwise, it is 0.
</p>

<p align="justify">
    The generated dataset is used to create an instance of the `NeuronalNetwork` class, `NN`. The `NeuronalNetwork` object is initialized with the generated `x` and `y` values, as well as other parameters such as the number of training epochs (`epoch`), the chosen activation function (`act_func`), and the number of weights (`n_weights`).
</p>

<p align="justify">
    After initializing the neural network, the `attemp` method is called, allowing for interactive testing of the trained network. The user can input values for prediction, and the corresponding output will be displayed. The user can also enter specific commands, such as "DATA", to view a subset of the training data or "W" to view the final weights and bias.
</p>

<p align="justify">
    Overall, this code provides a simple neural network implementation and a data generator to train and test the network. You can modify the parameters and experiment with different datasets and configurations to observe the network's performance.
</p>

<p align="center">
    <img src="divider.png" alt="Divider" width="70%">
</p>

<div align="center">
    <h3>Happy Coding! :rocket:</h3>
</div>

<p align="center">
    <img src="divider.png" alt="Divider" width="100%">
</p>
