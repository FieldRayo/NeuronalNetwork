commands_help = {
    "read_file": """\
    Command: read_file
    
    The 'read_file' command is used to execute commands from a text file. This is useful when you have multiple commands that you want to execute sequentially, and you want to avoid typing them directly into the console.
    
    Syntax:
    
    read_file --file 'file_name'
    
      - 'file_name': The name of the text file that contains the commands to be executed.
    
    Usage Example:
    
    Let's assume you have a text file named 'commands.txt' with the following content:
    
    create_net --name NN1 --n_inputs 2 --n_hidden [4, 6, 4] --n_outputs 1
    forward --name NN1 --input [[0.2, 0.3], [0.8, 0.5], [0.6, 0.1]]
    
    To execute the commands contained in the 'commands.txt' file, you can use the 'read_file' command as follows:
    
    read_file --file 'commands.txt'
    
    Notes:
    
    - The commands in the file should be written on separate lines, one per line.
    - The commands must be written in accordance with the correct syntax and format.
    - Each command must include the required parameters and their corresponding values, if applicable.
    - If a command contains errors or is not properly formatted, the execution will stop, and an error message will be displayed.
    
    Important:
    It is crucial to exercise caution when executing commands from a file, especially if the file comes from unknown or untrusted sources. The commands contained in the file will have the same effect as if they were executed directly in the console. Therefore, it is recommended to ensure that the commands are safe and well-formatted before executing them.
    """,
    
    "create_file": """\
    Command: create_file
    
    The 'create_file' command is used to create a text file in which commands can be written and later executed using the 'read_file' command. This is useful for organizing and storing a set of commands that you may want to reuse or execute multiple times.
    
    Syntax:
    
    create_file --file 'file_name'
    
      - 'file_name': The name of the text file to be created. It should have a valid file name without any extension.
    
    Usage Example:
    
    To create a new text file named 'my_commands.txt', you can use the 'create_file' command as follows:
    
    create_file --file 'my_commands'
    
    After running this command, a new file named 'my_commands.txt' will be created. You can then open this file with a text editor and write your desired commands on separate lines.
    
    Important Notes:
    
    - Each command should be written on a separate line in the text file.
    - Ensure that the commands written in the file are properly formatted and follow the correct syntax.
    - The 'read_file' command can be used later to execute the commands written in the file and perform the desired actions.
    
    Best Practices:
    
    - Use descriptive and meaningful names for the text files to help you remember the purpose of each file.
    - Organize your commands logically and separate them with blank lines or comments for better readability.
    
    Safety Tips:
    
    - Be cautious when executing commands from files, especially if the file comes from unknown or untrusted sources.
    - Before executing commands from a file, review the contents to ensure they are safe and will not cause unintended consequences.
    
    Remember that the 'create_file' command is intended for creating text files for storing commands. It does not execute the commands directly; you will need to use the 'read_file' command to execute the commands from the created file.
    """,
    
    "create_net": """\
    Command: create_net
    
    The 'create_net' command is used to create a new neural network with the specified configuration and architecture.
    
    Syntax:
    
    create_net --name 'name' (default='NN1') --n_inputs 'value' (default=2) --n_hidden 'value' (default=[4, 6, 4]) --n_outputs 'value' (default=1)
    
      - 'name': The name of the neural network to be created. The name must be a unique identifier for the network.
    
      - 'n_inputs': The number of input nodes in the neural network. It should be an integer value. Default value is 2.
    
      - 'n_hidden': The number of nodes in each hidden layer of the neural network. It should be a list of integers. Default value is [4, 6, 4].
    
      - 'n_outputs': The number of output nodes in the neural network. It should be an integer value. Default value is 1.
    
    Usage Example:
    
    To create a new neural network with the name 'NN1', 3 input nodes, 2 hidden layers with 5 nodes each, and 2 output nodes, use the 'create_net' command as follows:
    
    create_net --name 'NN1' --n_inputs 3 --n_hidden [5, 5] --n_outputs 2
    
    The command will create a neural network with the specified architecture and store it under the name 'NN1'. The neural network is now ready for further operations, such as forward propagation and training.
    
    Important Notes:
    
    - The 'name' parameter must be unique and should not match any existing neural network's name.
    - The 'n_inputs', 'n_hidden', and 'n_outputs' parameters determine the network's architecture and should be specified according to the problem's requirements.
    
    Best Practices:
    
    - Before creating a neural network, define the number of input nodes, hidden layers, and output nodes based on the characteristics of your data and the complexity of the problem.
    
    Safety Tips:
    
    - Avoid using the same name for different neural networks to prevent conflicts in managing and accessing the networks.
    - Make sure to set appropriate values for 'n_inputs', 'n_hidden', and 'n_outputs' to ensure that the network architecture suits the problem at hand.
    
    Please note that creating a neural network is the first step towards building a powerful machine learning model. After creating the network, you can perform various operations, such as forward propagation, training, and evaluation.
    """,
    
    "forward": """\
    Command: forward
    
    The 'forward' command is used to perform forward propagation on a previously created neural network. Forward propagation is the process of passing input data through the neural network to obtain the output prediction.
    
    Syntax:
    
    forward --name 'name' --input list
    
      - 'name': The name of the neural network on which forward propagation will be performed. The neural network must have been created using the 'create_net' command.
      
      - 'input': The input data for which you want to perform forward propagation. It should be a list containing the input values in the same format as the number of input neurons in the neural network.
    
    Usage Example:
    
    Let's assume you have created a neural network with the name 'NN1' using the 'create_net' command. The network has two input neurons, so you want to perform forward propagation for the input [0.2, 0.3]. To do this, use the 'forward' command as follows:
    
    forward --name 'NN1' --input [0.2, 0.3]
    
    The command will execute forward propagation on the 'NN1' neural network with the input [0.2, 0.3]. The neural network will process the input data and produce an output prediction.
    
    Important Notes:
    
    - The 'name' parameter must match the name of an existing neural network created with the 'create_net' command.
    - The 'input' parameter should be a list containing the input values in the same order as the number of input neurons in the neural network.
    - The 'forward' command only performs forward propagation and does not update the neural network's weights or make any changes to the network's internal state.
    
    Best Practices:
    
    - Double-check the 'name' parameter to ensure it matches the correct neural network's name.
    - Verify that the 'input' data is correctly formatted and contains the expected number of input values.
    
    Safety Tips:
    
    - Before performing forward propagation, ensure that the neural network has been properly initialized with the correct architecture and weights.
    - If you encounter any issues or unexpected results, review the neural network's architecture and weights to identify potential problems.
    
    Please note that forward propagation is an essential step in using neural networks for prediction tasks. Make sure to provide valid and appropriate input data for accurate predictions.
    """,
    
    "backpropagation": """\
    Command: backpropagation
    
    The 'backpropagation' command is used to perform backpropagation on a previously created neural network. Backpropagation is a critical step in training neural networks, where the network learns from its mistakes and updates its weights to improve its performance.
    
    Syntax:
    
    backpropagation --name 'name'
    
      - 'name': The name of the neural network on which backpropagation will be performed. The neural network must have been created using the 'create_net' command.
    
    Usage Example:
    
    Suppose you have created a neural network with the name 'NN1' using the 'create_net' command. To perform backpropagation on this neural network, use the 'backpropagation' command as follows:
    
    backpropagation --name 'NN1'
    
    The command will execute backpropagation on the 'NN1' neural network. During this process, the neural network will use the difference between its output and the expected target values to adjust its weights and minimize the error.
    
    Important Notes:
    
    - The 'name' parameter must match the name of an existing neural network created with the 'create_net' command.
    - Backpropagation is crucial for training neural networks and improving their performance by reducing prediction errors.
    - The 'backpropagation' command updates the neural network's internal state, but it does not change the network's architecture or hyperparameters.
    
    Best Practices:
    
    - Ensure that the neural network has been properly initialized with the correct architecture and weights before performing backpropagation.
    - Use a sufficient amount of training data and appropriate learning rate to achieve better convergence during backpropagation.
    
    Safety Tips:
    
    - Be patient during the backpropagation process, as it may take several iterations to achieve the desired level of error reduction.
    - Monitor the neural network's progress during training to identify any potential issues or anomalies.
    
    Please note that backpropagation is a critical step in the training process of neural networks. After running the 'backpropagation' command, the neural network's weights will be updated, and it will be better equipped to make accurate predictions on new data.
    """,
    
    "gradientdescent": """\
    Command: gradientdescent
    
    The 'gradientdescent' command is used to perform gradient descent on a previously created neural network. Gradient descent is an optimization algorithm used to update the network's weights during the training process, helping the neural network converge to a better set of weights that minimize prediction errors.
    
    Syntax:
    
    gradientdescent --name 'name' --lr float
    
      - 'name': The name of the neural network on which gradient descent will be performed. The neural network must have been created using the 'create_net' command.
    
      - 'lr': The learning rate, which determines the step size for weight updates during gradient descent. It should be a positive floating-point number.
    
    Usage Example:
    
    Suppose you have created a neural network with the name 'NN1' using the 'create_net' command. To perform gradient descent on this neural network with a learning rate of 0.01, use the 'gradientdescent' command as follows:
    
    gradientdescent --name 'NN1' --lr 1
    
    The command will execute gradient descent on the 'NN1' neural network with the specified learning rate. During this process, the neural network's weights will be updated in the direction that reduces prediction errors, helping the network learn from the training data.
    
    Important Notes:
    
    - The 'name' parameter must match the name of an existing neural network created with the 'create_net' command.
    - The learning rate ('lr') is a crucial hyperparameter in gradient descent. A large learning rate can lead to overshooting, while a small one can result in slow convergence.
    
    Best Practices:
    
    - Experiment with different learning rates to find the one that results in the fastest convergence without overshooting.
    - Combine gradient descent with other optimization techniques, such as momentum or adaptive learning rate methods, to enhance training performance.
    
    Safety Tips:
    
    - Before performing gradient descent, ensure that the neural network has been properly initialized and trained with the 'backpropagation' and 'train_net' commands.
    - Monitor the training progress and keep track of the error reduction to assess the effectiveness of gradient descent.
    
    Please note that gradient descent is a critical optimization algorithm used in training neural networks. It plays a vital role in updating the network's weights and fine-tuning the model to achieve better performance on unseen data.
    """,
    
    "get_value": """\
    Command: get_value
    
    The 'get_value' command is used to retrieve specific values from a previously created neural network.
    
    Syntax:
    
    get_value --name 'name' --value 'value' --index 'index'
    
      - 'name': The name of the neural network from which to retrieve the value. The neural network must have been created using the 'create_net' command.
    
      - 'value': The name of the specific value to retrieve from the neural network. It can be one of the following options:
        - 'weights': Retrieve the weights of the connections between nodes in the network.
        - 'bias': Retrieve the bias values for each node in the network.
        - 'activations': Retrieve the activation values of the nodes in the network.
        - 'deltas': Retrieve the delta values, which are used in backpropagation.
        - 'derivatives': Retrieve the derivatives of the weights with respect to the error during backpropagation.
    
      - 'index': The index or range of indices for which to retrieve the values. It can be specified as a single number, a range (start-end), or '*' to retrieve all values.
    
    Usage Example:
    
    Suppose you have created a neural network with the name 'NN1' using the 'create_net' command. To retrieve the weights of the connections between nodes, use the 'get_value' command as follows:
    
    get_value --name 'NN1' --value 'weights' --index '2-5'
    
    The command will retrieve the weights of the connections between nodes 2 to 5 (inclusive) in the 'NN1' neural network.
    
    Important Notes:
    
    - The 'name' parameter must match the name of an existing neural network created with the 'create_net' command.
    - The 'value' parameter specifies which values to retrieve, and it should be one of the valid options mentioned above.
    
    Best Practices:
    
    - Use the 'get_value' command to inspect and analyze the neural network's internal parameters and activation values during the training process.
    
    Safety Tips:
    
    - Ensure that the 'name' parameter corresponds to an existing neural network to avoid errors.
    - Check the 'value' options to ensure you are retrieving the correct values you need for analysis or debugging.
    
    Please note that the 'get_value' command is a useful tool for exploring and understanding the behavior of the neural network during training and prediction. It allows you to access essential parameters and values within the network for further analysis and insights.
    """,
    
    "set_value": """\
    Command: set_value
    
    The 'set_value' command is used to modify specific values in a previously created neural network.
    
    Syntax:
    
    set_value --name 'name' --value 'value' --new_value 'new_value'
    
      - 'name': The name of the neural network in which to modify the value. The neural network must have been created using the 'create_net' command.
    
      - 'value': The name of the specific value to modify in the neural network. It can be one of the following options:
        - 'weights': Modify the weights of the connections between nodes in the network.
        - 'bias': Modify the bias values for each node in the network.
        - 'activations': Modify the activation values of the nodes in the network.
    
      - 'new_value': The new value or values to set for the specified parameter. The format of 'new_value' should match the original parameter's format.
    
    Usage Example:
    
    Suppose you have created a neural network with the name 'NN1' using the 'create_net' command. To modify the weights of the connections between nodes, use the 'set_value' command as follows:
    
    set_value --name 'NN1' --value 'weights' --new_value '[[0.5, 0.2], [0.8, -0.3]]'
    
    The command will set new weights for the connections between nodes in the 'NN1' neural network.
    
    Important Notes:
    
    - The 'name' parameter must match the name of an existing neural network created with the 'create_net' command.
    - The 'value' parameter specifies which values to modify, and it should be one of the valid options mentioned above.
    - Ensure that the format of 'new_value' matches the original parameter's format (e.g., list for weights and activations, single value for bias).
    
    Best Practices:
    
    - Use the 'set_value' command to fine-tune the neural network's parameters or explore different configurations during experimentation.
    
    Safety Tips:
    
    - Double-check the 'name' parameter to ensure you are modifying values in the intended neural network.
    - Be cautious when modifying values, as incorrect changes can lead to unexpected behavior during training and prediction.
    
    Please note that the 'set_value' command allows you to customize and experiment with the neural network's internal parameters, such as weights, bias, and activations, to optimize its performance for specific tasks.
    """,
    
    "show_nn": """\
    Command: show_nn
    
    The 'show_nn' command is used to display the names of all created neural networks.
    
    Syntax:
    
    show_nn
    
    Usage Example:
    
    Simply type 'show_nn' to execute the command. The names of all created neural networks will be displayed.
    
    Description:
    
    The 'show_nn' command is a simple and convenient way to view the names of all neural networks that have been created using the 'create_net' command. It helps keep track of the existing neural networks in the current session.
    
    Important Notes:
    
    - The 'show_nn' command does not take any additional parameters.
    - The names of neural networks displayed are the unique identifiers specified when creating the networks using the 'create_net' command.
    
    Best Practices:
    
    - Use the 'show_nn' command whenever you want to quickly check the names of all existing neural networks in the current session.
    
    Safety Tips:
    
    - Double-check the names of neural networks shown to ensure they match the ones you have created.
    
    Please note that the 'show_nn' command is a simple utility command that provides an overview of the available neural networks and their respective names in the current environment.
    """,
    "show_data": """\
    Command: show_data
    
    The 'show_data' command is used to display specific data from a previously created neural network.
    
    Syntax:
    
    show_data --name 'name' --value 'value' --index 'index'
    
      - 'name': The name of the neural network from which to retrieve the data. The neural network must have been created using the 'create_net' command.
    
      - 'value': The name of the specific data to retrieve from the neural network. It can be one of the following options:
        - 'weights': Display the weights of the connections between nodes in the network.
        - 'bias': Display the bias values for each node in the network.
        - 'activations': Display the activation values of the nodes in the network.
        - 'derivatives': Display the derivative values computed during backpropagation.
        - 'deltas': Display the gradient descent bias values.
    
      - 'index' (optional): The index or range of indices for the specific data to display. It can be a single number, a range (start-end), or '*' to display all values.
    
    Usage Example:
    
    Suppose you have created a neural network with the name 'NN1' using the 'create_net' command. To view the weights of the connections between nodes, use the 'show_data' command as follows:
    
    show_data --name 'NN1' --value 'weights'
    
    The command will display the weights of the connections in the 'NN1' neural network.
    
    Important Notes:
    
    - The 'name' parameter must match the name of an existing neural network created with the 'create_net' command.
    - The 'value' parameter specifies which data to display and should be one of the valid options mentioned above.
    - If 'index' is not provided, all values for the specified 'value' will be displayed.
    
    Best Practices:
    
    - Use the 'show_data' command to inspect the internal data of the neural network, such as weights, bias, and activations, to gain insights into its behavior.
    
    Safety Tips:
    
    - Double-check the 'name' parameter to ensure you are accessing data from the intended neural network.
    - Exercise caution when displaying large datasets to avoid overwhelming the output.
    
    Please note that the 'show_data' command provides a convenient way to explore the internal state of the neural network and understand how it learns and makes predictions.
    """,
    "len_data": """\
    Command: len_data
    
    The 'len_data' command is used to display the length of specific data from a previously created neural network.
    
    Syntax:
    
    len_data --name 'name' --value 'value'
    
      - 'name': The name of the neural network from which to retrieve the data length. The neural network must have been created using the 'create_net' command.
    
      - 'value': The name of the specific data for which the length needs to be determined. It can be one of the following options:
        - 'weights': Length of the weights of the connections between nodes in the network.
        - 'bias': Length of the bias values for each node in the network.
        - 'activations': Length of the activation values of the nodes in the network.
        - 'derivatives': Length of the derivative values computed during backpropagation.
        - 'deltas': Length of the gradient descent bias values.
    
    Usage Example:
    
    Suppose you have created a neural network with the name 'NN1' using the 'create_net' command. To view the length of the bias values in the 'NN1' neural network, use the 'len_data' command as follows:
    
    len_data --name 'NN1' --value 'bias'
    
    The command will display the number of bias values in the 'NN1' neural network.
    
    Important Notes:
    
    - The 'name' parameter must match the name of an existing neural network created with the 'create_net' command.
    - The 'value' parameter specifies which data to examine and should be one of the valid options mentioned above.
    
    Best Practices:
    
    - Use the 'len_data' command when you need to know the size or number of elements in specific data within the neural network.
    
    Safety Tips:
    
    - Double-check the 'name' parameter to ensure you are accessing data from the intended neural network.
    
    Please note that the 'len_data' command provides a quick way to retrieve the length of specific data within the neural network, helping to gain insights into its structure and complexity.
    """,
    "train_net": """\
    Command: train_net
    
    The 'train_net' command is used to train a previously created neural network with backpropagation using a specific learning rate and error tolerance.
    
    Syntax:
    
    train_net --name 'name' --lr float --err_max float
    
      - 'name': The name of the neural network to be trained. The neural network must have been created using the 'create_net' command.
    
      - 'lr': The learning rate for gradient descent. It is a floating-point value between 0 and 1, representing the step size at each iteration during training.
    
      - 'err_max': The maximum allowable error during training. It is a floating-point value between 0 and 1, indicating the desired level of accuracy in the predictions.
    
    Usage Example:
    
    Suppose you have created a neural network with the name 'NN1' using the 'create_net' command and you want to train it with a learning rate of 0.01 and a maximum error of 0.001. Use the 'train_net' command as follows:
    
    train_net --name 'NN1' --lr 4 --err_max 4
    
    The command will initiate the training process for the 'NN1' neural network with the specified learning rate and error tolerance.
    
    Important Notes:
    
    - The 'name' parameter must match the name of an existing neural network created with the 'create_net' command.
    - The 'lr' parameter should be carefully chosen to ensure efficient learning without overshooting or diverging.
    - The 'err_max' parameter determines the desired accuracy level in the predictions.
    
    Best Practices:
    
    - Experiment with different learning rates and error tolerances to find the optimal training parameters for the neural network.
    
    Safety Tips:
    
    - Double-check the 'name' parameter to ensure you are training the intended neural network.
    - Be cautious with the choice of learning rate to prevent issues like vanishing or exploding gradients.
    
    Please note that the 'train_net' command initiates the training process for the specified neural network, allowing it to learn from the provided data and adjust its internal parameters to make accurate predictions.
    """,
    "show_graphic": """\
    Command: show_graphic
    
    The 'show_graphic' command is used to display a graph of the training errors for a previously trained neural network.
    
    Syntax:
    
    show_graphic --name 'name' --graphic 'graphic' --type 'type'
    
      - 'name': The name of the neural network for which the training errors will be displayed. The neural network must have been trained using the 'train_net' command.
    
      - 'graphic': The type of training errors to display. It can be one of the following options:
        - 'errors': Display the errors at each iteration during training.
        - 'mse': Display the Mean Squared Error (MSE) at each iteration during training.
    
      - 'type': The type of graphic to use for visualization. It can be one of the following options:
        - 'plot': Display the training errors as a line plot.
        - 'scatter': Display the training errors as a scatter plot.
    
    Usage Example:
    
    Suppose you have trained a neural network with the name 'NN1' using the 'train_net' command and you want to visualize the training errors as a line plot. Use the 'show_graphic' command as follows:
    
    show_graphic --name 'NN1' --graphic 'errors' --type 'plot'
    
    The command will generate a line plot showing the training errors at each iteration during the training of the 'NN1' neural network.
    
    Important Notes:
    
    - The 'name' parameter must match the name of an existing neural network that has been trained using the 'train_net' command.
    - The 'graphic' parameter specifies the type of training errors to visualize.
    - The 'type' parameter determines the type of plot to use for visualization.
    
    Best Practices:
    
    - Use the 'show_graphic' command after training a neural network to understand the training progress and identify potential issues.
    
    Safety Tips:
    
    - Double-check the 'name' parameter to ensure you are visualizing the training errors for the intended neural network.
    
    Please note that the 'show_graphic' command provides a visual representation of the training errors, helping to assess the training performance and make informed decisions to improve the neural network's accuracy.
    """,
}
