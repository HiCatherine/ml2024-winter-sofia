"""
The program asks the user for input N (positive integer) and reads it.

Then the program asks the user for input k (positive integer) and reads it.

Then the program asks the user to provide N (x, y) points (one by one) and reads all of them: first: x value, then: y value for every point one by one. X and Y are the real numbers.

In the end, the program asks the user for input X and outputs: the result (Y) of k-NN Regression if k <= N, or any error message otherwise.

The basic functionality of data processing (data initialization, data insertion, data calculation) should be done using Numpy library as much as possible (note: you can combine with OOP from the previous task).

"""
import numpy as np

class KNNRegression:
    def __init__(self, k, X_train, Y_train):
        self.k = k
        self.X_train = X_train
        self.Y_train = Y_train

    def fit(self, X_train, Y_train):
        self.X_train = np.array(X_train)
        self.Y_train = np.array(Y_train)

    def predict(self, X_test):
        distances = np.array([(x_train - X_test)**2 for x_train in self.X_train])
        nearest_indices = np.argsort(distances)[:self.k]
        nearest_labels = self.Y_train[nearest_indices]
        return np.mean(nearest_labels)    


def main():
    N = prompt_for_number("N", is_int=True, is_positive=True, additional_prompt=" for the number of pairs of inputs")
    k = prompt_for_number("k", is_int=True, is_positive=True, additional_prompt=" for the k-NN regression")

    numbers = np.empty((0, 2))
    for i in range(N):
        x = prompt_for_number("x", additional_prompt=f" in the {i + 1}-th pair")
        y = prompt_for_number("y", additional_prompt=f" in the {i + 1}-th pair")
        numbers = np.append(numbers, [[x, y]], axis=0)

    X_train = numbers[:, 0]
    Y_train = numbers[:, 1]
    regr = KNNRegression(k, X_train, Y_train)
    
    X_test = prompt_for_number("X", additional_prompt=" as the test data input")
    Y_test = regr.predict(X_test)
    print(f"The predicted output value for X is {Y_test}")

    
def prompt_for_number(name, additional_prompt="", is_int=False, is_positive=False):
    while True:
        try:
            ask = input(f"Enter value for {name}" + additional_prompt + "\n")
            if (is_int):
                n = int(ask)
            else:
                n = float(ask)
            if (is_positive) and n <= 0:
                raise ValueError("Number must be positive\n")
            else:
                break
        except ValueError:
            print("Please enter a valid number\n")
    return n


if __name__ == "__main__":
    main()
