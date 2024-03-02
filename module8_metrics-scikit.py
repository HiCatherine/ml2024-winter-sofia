"""
The program asks the user for input N (positive integer) and reads it.

Then the program asks the user to provide N (x, y) points (one by one) and reads all of them: first: x value, then: y value for every point one by one. X is treated as the ground truth (correct) class label and Y is treated as the predicted class. Both X and Y are either 0 or 1.

In the end, the program outputs: the Precision and Recall based on the inputs.

The basic functionality of data processing (data initialization, data insertion), should be done using Numpy library while the computation (ML) part should be done using Scikit-learn library as much as possible (note: you can combine with what you've done from the previous tasks).
"""
import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    N = prompt_for_number("N", is_int=True, is_positive=True, additional_prompt=" for the number of pairs of inputs")

    truth = np.array([])
    predicted = np.array([])
    for i in range(N):
        x = prompt_for_number("x", additional_prompt=f" (the ground truth value) in the {i + 1}-th pair")
        y = prompt_for_number("y", additional_prompt=f" (the predicted value) in the {i + 1}-th pair")
        truth = np.append(truth, x)
        predicted = np.append(predicted, y)

    precision = precision_score(truth, predicted, average='macro')
    recall = recall_score(truth, predicted, average='macro')
    print(f"The precision is {precision} and recall is {recall}")
    
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
