def duplicates(lst):
    s1 = set(lst)
    result = list(s1)
    return result

def main():
    num = input("Enter ten numbers separated by spaces: ")
    input_list = list(map(int, num.split()))

    num_without_dup = duplicates(input_list)

    print("The distinct numbers are:", *num_without_dup)

main()
