# reverse words in a string
s = "Reverse this string"

def reverse_words(s):
    # Convert the string to a list of characters
    char_list = list(s)
    
    left = 0
    right = len(char_list) - 1

    while left < right:
        # Swap the characters
        char_list[left], char_list[right] = char_list[right], char_list[left]
        left += 1
        right -= 1
    
    # Convert the list back to a string
    return ''.join(char_list)

print(reverse_words(s))