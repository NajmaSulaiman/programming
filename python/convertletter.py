user_input = input("Enter a word: ")

vowels = "aeiouAEIOU"
result_word = ""

for char in user_input:
    if char in vowels:
        result_word += char.upper()
    else:
        result_word += char

print("Result:", result_word)

