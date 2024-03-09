"""
The program asks the user for input N (positive integer) and reads it.

Then the program asks the user to provide N (x, y) pairs (one by one) and reads all of them: first: x value, then: y value for every pair one by one. X is treated as the input feature and Y is treated as the class label. X is a real number, Y is a non-negative integer.

This set of pairs constitutes the training set TrainS = {(x, y)_i}, i = 1..N.

Then the program asks the user for input M (positive integer) and reads it.

Then the program asks the user to provide M (x, y) pairs (one by one) and reads all of them: first: x value, then: y value for every pair one by one. X is treated as the input feature and Y is treated as the class label. X is a real number, Y is a non-negative integer.

This set of pairs constitutes the test set TestS = {(x, y)_i}, i = 1..M.

In the end, the program outputs: the best k for the kNN Classification method and the corresponding test accuracy. kNN Classifier should be trained on pairs from TrainS, tested on x values from TestS and compared with y values from TestS.

The basic functionality of data processing (data initialization, data insertion), should be done using Numpy library while the computation (ML) part should be done using Scikit-learn library as much as possible (note: you can combine with what you've done from the previous tasks). 

Note: you can try the following range of k: 1 <= k <= 10.
"""
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def main():
    N = prompt_for_number("N", is_int=True, condition=lambda x: x > 0, additional_prompt=" for the number of pairs of inputs as training data")
    TrainS = np.array([prompt_for_pair(i) for i in range(N)])

    M = prompt_for_number("M", is_int=True, condition=lambda x: x > 0, additional_prompt=" for the number of pairs of inputs as test data")
    TestS = np.array([prompt_for_pair(i) for i in range(M)])

    best_k, best_accuracy = find_best_k(TrainS, TestS)

    print(f"The best k for the kNN Classification method is k = {best_k} with a test accuracy of {best_accuracy}")

def find_best_k(TrainS, TestS):
    X_train, y_train = TrainS[:, 0].reshape(-1, 1), TrainS[:, 1]
    X_test, y_test = TestS[:, 0].reshape(-1, 1), TestS[:, 1]

    best_k, best_accuracy = 0, 0
    for k in range(1, 11):
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train, y_train)
        y_pred = knn.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        if accuracy > best_accuracy:
            best_k, best_accuracy = k, accuracy
    return best_k, best_accuracy

def prompt_for_number(name, additional_prompt="", is_int=False, condition=lambda x: True):
    while True:
        try:
            ask = input(f"Enter value for {name}" + additional_prompt + "\n")
            if (is_int):
                n = int(ask)
            else:
                n = float(ask)
            if not condition(n):
                raise ValueError("Number does not satisfy requirement\n")
            else:
                break
        except ValueError:
            print("Please enter a valid number\n")
    return n

def prompt_for_pair(i):
    x = prompt_for_number("x", additional_prompt=f" (the input feature) in the {i + 1}-th pair")
    y = prompt_for_number("y", is_int=True, condition=lambda x: x >= 0, additional_prompt=f" (the class label) in the {i + 1}-th pair")
    return [x, y]

if __name__ == "__main__":
    main()
