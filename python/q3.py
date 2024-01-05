def eliminate_duplicates(lst):
    unique_values = set(lst)
    result = list(unique_values)
    return result

def main():
    
    input_list = []
    for i in range(10):
        num = int(input("Enter an integer: "))
        input_list.append(num)
    result_list = eliminate_duplicates(input_list)

    
    print("Original list:", input_list)
    print("List with duplicates eliminated:", result_list)


main()
