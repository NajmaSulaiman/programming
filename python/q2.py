def index_of_smallest_element(lst):
    if not lst:
        return None

    
    min_index = 0
    for i in range(1, len(lst)):
        if lst[i] < lst[min_index]:
            min_index = i

    return min_index

def main():
    input_list = []
    for i in range(10):
        num = int(input("Enter a number: "))
        input_list.append(num)

    result_index = index_of_smallest_element(input_list)

    if result_index is not None:
        
        print("List:", input_list)
        print("Index of the smallest element:", result_index)
    else:
        print("The list is empty.")


main()
