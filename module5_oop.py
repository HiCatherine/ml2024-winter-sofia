class NumberSearch:
    def __init__(self):
        self.numbers = []

    def get_number_of_elements(self):
        while True:
            try:
                n = int(input("Enter the number of elements (N): "))
                if n > 0:
                    return n
                else:
                    print("Please enter a positive integer for N.")
            except ValueError:
                print("Please enter a valid integer for N.")

    def get_numbers(self, n):
        for i in range(n):
            while True:
                try:
                    num = float(input(f"Enter {i + 1}-th number: "))
                    break
                except ValueError:
                    print("Please enter a valid number.")
            self.numbers.append(num)

    def search_number(self):
        while True:
            try:
                x = int(input("Enter the number to search for (X): "))
                return x
            except ValueError:
                print("Please enter a valid integer for X.")

    def find_index(self, x):
        if x in self.numbers:
            return self.numbers.index(x) + 1
        else:
            return -1

def main():
    number_search = NumberSearch()

    n = number_search.get_number_of_elements()
    number_search.get_numbers(n)

    x = number_search.search_number()

    index = number_search.find_index(x)

    if index != -1:
        print(f"Index of {x} (from 1 to N): {index}")
    else:
        print("-1")


if __name__ == "__main__":
    main()
