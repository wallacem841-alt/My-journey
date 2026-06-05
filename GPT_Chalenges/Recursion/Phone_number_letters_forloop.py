digit_to_letters = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}

def letter_combinations(digits):
    if not digits:
        return []
    
    # Start with an initial list containing an empty combination
    combinations = [""]

    # Iterate over each digit in the input
    for digit in digits:
        # Get the corresponding letters for this digit
        letters = digit_to_letters.get(digit, [])
        # Temporary list to hold the new combinations
        new_combinations = []
        
        # Create new combinations by appending each letter to each combination so far
        for combination in combinations:
            for letter in letters:
                new_combinations.append(combination + letter)
        
        # Update the combinations list to the new combinations
        combinations = new_combinations

    return combinations

result = letter_combinations("2324")
print(result)