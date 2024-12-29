
class Perceptron:
    def __init__(self, num_inputs):
        self.weights = [0 for _ in range(num_inputs)]
        self.bias = 0

    def forward(self, inputs):
        weighted_sum = self.bias
        for i, _input in enumerate(inputs):
            weighted_sum += _input * self.weights[i]
        
        if weighted_sum > 0:
            return 1
        else:
            return 0

    def update(self, inputs, correct_output):
        error = correct_output - self.forward(inputs)

        for i, _ in enumerate(self.weights):
            self.weights[i] += error * inputs[i]
        self.bias += error