"""
The program asks the user for input N (positive integer) and reads it

Then the program asks the user to provide N numbers (one by one) and reads all of them (again, one by one)

In the end, the program asks the user for input X (integer) and outputs: 
"-1" if there were no such X among N read numbers, 
or the index (from 1 to N) of this X if the user inputed it before.
"""
def main():
    while True:
        try:
            n = int(input("Enter the number of elements (N): "))
            if n > 0:
                print("Please enter a positive integer for N.")
                break
        except ValueError:
            print("Please enter a valid integer for N.")

    numbers = []
    for i in range(n):
        while True:
            try:
                num = float(input(f"Enter {i + 1}-th number: "))
                break
            except ValueError:
                print("Please enter a valid number.")
        numbers.append(num)

    while True:
        try:
            x = int(input("Enter the number to search for (X): "))
            break
        except ValueError:
            print("Please enter a valid integer for X.")

    if x in numbers:
        print(f"Index of {x} (from 1 to N): {numbers.index(x) + 1}")
    else:
        print("-1")

if __name__ == "__main__":
    main()
