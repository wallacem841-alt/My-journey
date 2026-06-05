#palindrome challenge
import re
input_word = 'radar:'

def palindrome(word):
    word = word.lower()

    result_word = re.sub(r'[^a-z0-9]', '', word)

    return result_word == result_word[::-1]
    
result = palindrome(input_word)

print(result)