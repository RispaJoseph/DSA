# def reverse(word):
#     return word[::-1] 

# word = input("Enter you input: ")
# reversed_string = reverse(word)
# print(reversed_string)


# Using for loop

def reverse_string(word):
    reverse_list = ""

    for char in word:
        reverse_list = char + reverse_list
    return reverse_list

user_input = input("Enter something : ")
reverse_it = (reverse_string(user_input))
print(reverse_it)