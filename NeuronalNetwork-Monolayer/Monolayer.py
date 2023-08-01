import numpy as np
import matplotlib.pyplot as plt

inputs = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
y = np.array([[0], [1], [1], [0]])

# XD 2
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Layers
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # Weights
        self.W1 = np.random.rand(self.input_size, self.hidden_size)
        self.W2 = np.random.rand(self.hidden_size, self.output_size)

        # Ec
        self.sigmoid = lambda x: 1 / (1 + np.exp(-x))
        self.sigmoid_der = lambda x: x * (1 - x)
        self.mse = lambda output, target: np.mean((output - target) ** 2) / 2

    def forward(self, X):
        self.z1 = X @ self.W1
        self.a1 = self.sigmoid(self.z1)
        self.z2 = self.a1 @ self.W2
        self.output = self.sigmoid(self.z2)

        return self.output

    def backprop(self, X, y, lr):
        # Derivate Weight 2: (output - y) * sigm(z2) * a1
        output = self.forward(X)
        error_out = output - y
        delta_out = error_out * self.sigmoid_der(output)
        W2_der = self.a1.T @ delta_out

        # Derivate Weight 1: (output - y) * simg(z2) * W2 * sigm(z1) * inputs
        error_hidden = delta_out @ self.W2.T
        delta_hidden = error_hidden * self.sigmoid_der(self.a1)
        W1_der = inputs.T @ delta_hidden

        # Gradient decent
        self.W2 -= W2_der * lr
        self.W1 -= W1_der * lr

        return self.mse(output, y)


nn = NeuralNetwork(3, 3, 1)
errors = []
error = 1

error_tol = 0.001
while error > error_tol:
    error = nn.backprop(inputs, y, 0.7)
    errors.append(error)
    print(f"\rLoading Training: {round((error_tol / error) * 100, 10)}%", end="")

print("\n")
print(nn.forward(inputs))

x_axis = range(0, len(errors))
plt.plot(x_axis, errors)
plt.show()