from module5_mod import NumberSearch

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
