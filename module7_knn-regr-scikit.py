"""
The program asks the user for input N (positive integer) and reads it.

Then the program asks the user for input k (positive integer) and reads it.

Then the program asks the user to provide N (x, y) points (one by one) and reads all of them: first: x value, then: y value for every point one by one. X and Y are the real numbers.

In the end, the program asks the user for input X and outputs: the result (Y) of k-NN Regression if k <= N, or any error message otherwise.

Additionally, if the program outputs Y, provide the coefficient of determination.

The basic functionality of data processing (data initialization, data insertion), should be done using Numpy library while the computation (ML) part should be done using Scikit-learn library as much as possible (note: you can combine with what you've done from the previous task).
"""
import numpy as np
from sklearn.neighbors import KNeighborsRegressor

class KNNRegression:
    def __init__(self, k):
        self.k = k
        self.model = KNeighborsRegressor(n_neighbors=k)

    def fit(self, X_train, Y_train):
        self.model.fit(X_train, Y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)

def main():
    N = prompt_for_number("N", is_int=True, is_positive=True, additional_prompt=" for the number of pairs of inputs")
    k = prompt_for_number("k", is_int=True, is_positive=True, additional_prompt=" for the k-NN regression")

    numbers = np.empty((0, 2))
    for i in range(N):
        x = prompt_for_number("x", additional_prompt=f" in the {i + 1}-th pair")
        y = prompt_for_number("y", additional_prompt=f" in the {i + 1}-th pair")
        numbers = np.append(numbers, [[x, y]], axis=0)

    X_train = numbers[:, 0].reshape((-1, 1))
    Y_train = numbers[:, 1].reshape(-1)

    regr = KNNRegression(k)
    regr.fit(X_train, Y_train)
    
    x_test_num = prompt_for_number("X", additional_prompt=" as the test data input")
    X_test = np.array([x_test_num]).reshape(1, 1)
    Y_test = regr.predict(X_test)
    print(f"The predicted output value for X is {Y_test[0]}")

    
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
