import numpy as np
import matplotlib.pyplot as plt


# plt.scatter(X[:, 0], X[:, 1], c=y)
# plt.show()

# Test Commit

class NeuronalNetwork:
    def __init__(self, n_inputs=2, n_hidden=[4, 6, 4], n_outputs=1):
        # Layers
        self.n_inputs = n_inputs
        self.n_hidden = n_hidden
        self.n_outputs = n_outputs
        self.layers = [self.n_inputs] + self.n_hidden + [self.n_outputs]
        
        # Functions
        self.sigmoid = lambda x: 1 / (1 + np.exp(-x))
        self.sigmoid_der = lambda x: x * (1 - x)
        self.relu = lambda x: np.maximum(0, x)
        self.relu_der = lambda x: x > 0 * 1
        self.mse = lambda output, target: np.mean((output - target) ** 2) / 2
        
        # ec
        self.weights = []
        self.derivatives = []
        self.bias = []
        self.activations = []
        self.deltas = []
        
        self.main()
    
    def main(self):
        # Set Layers
        self.layers = [self.n_inputs] + self.n_hidden + [self.n_outputs]
        
        # set weights, derivatives y bias
        weights = []
        derivatives = []
        bias = []
        
        for i in range(len(self.layers) - 1):
            w = np.random.normal(scale=0.5, size=(self.layers[i], self.layers[i + 1]))
            d = np.zeros((self.layers[i], self.layers[i + 1]))
            b = np.zeros((1, self.layers[i + 1]))
            
            weights.append(w)
            derivatives.append(d)
            bias.append(b)
        
        self.weights = weights
        self.derivatives = derivatives
        self.bias = bias
        
        # Set activations
        activations = []
        
        for i in range(len(self.layers)):
            a = np.zeros((1, self.layers[i]))
            activations.append(a)
        
        self.activations = activations
        
        # Deltas (Gradient decent bias)
        deltas = []
        
        for i in range(len(bias)):
            d = np.zeros(bias[i].shape)
            deltas.append(d)
        
        self.deltas = deltas
    
    def forward(self, inputs):
        self.activations[0] = inputs
        z = (inputs @ self.weights[0]) + self.bias[0]
        a = self.sigmoid(z)
        self.activations[1] = a
        
        for i in range(len(self.layers) - 2):
            z = (a @ self.weights[i + 1]) + self.bias[i + 1]
            a = self.sigmoid(z)
            self.activations[i + 2] = a
        
        return self.activations[-1]
    
    def backprop(self, error):
        back = list(range(len(self.layers) - 1))
        back.reverse()
        
        for i in back:
            a = self.activations[i + 1]
            delta = error * self.sigmoid_der(a)
            self.deltas[i] = delta
            a_current = self.activations[i]
            d = np.dot(a_current.T, delta)
            self.derivatives[i] = d
            error = np.dot(delta, self.weights[i].T)
    
    def gradient_descent(self, lr):
        ajust = []
        for i in range(len(self.weights)):
            w = self.weights[i]
            d = self.derivatives[i]
            w -= d * lr
            ajust.append(w - d * lr)
            self.weights[i] = w
            self.bias[i] -= np.mean(self.deltas[i], axis=0, keepdims=True)
        return ajust
    
    def train(self, x, y, lr, err_max):
        err_mse = 1
        errors = []
        
        while err_mse > err_max:
            output = self.forward(x)
            error = output - y
            self.backprop(error)
            self.gradient_descent(lr)
            err_mse = self.mse(output, y)
            errors.append(err_mse)
            print(f"Mean Squared Error: {err_mse}\r", end="")
        
        x_axis = range(0, len(errors))
        return [x_axis, errors]

# nn = NeuronalNetwork(2, [4, 8, 4], 1)
# nn.train(X, y, 0.002, 0.0005)
