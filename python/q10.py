def cal(word_list, n):
    result = []
    for word in word_list:
        if len(word) > n:
            result.append(word)
    return result

word_list = input("Enter a list of words (separated by space): ").split()
n = int(input("Enter the minimum length (n): "))


filterr = cal(word_list, n)

print("words longer than",n,":")
print(filterr)

