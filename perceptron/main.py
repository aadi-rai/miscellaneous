from perceptron import Perceptron


test = Perceptron(2)

for i in range(99999):
    for p, q in [[0, 0], [0, 1], [1, 0], [1, 1]]:
        test.update([p, q], int(p or q))

    num_correct = 0
    for p, q in [[0, 0], [0, 1], [1, 0], [1, 1]]:
        if test.forward([p, q]) == int(p or q):
            num_correct += 1
    if num_correct == 4:
        print(f"100% accurate after {i+1} epochs")
        break
