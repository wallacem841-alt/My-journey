def letter_combinations(digits):
    # Define a dictionary to map digits to corresponding letters
    digit_to_char = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }

    # Base case: if there are no digits, return an empty list
    if not digits:
        return []
    
    # Recursive function to generate combinations
    def backtrack(index, path):
        # If the path length matches the digits length, add it to results
        if index == len(digits):
            combinations.append("".join(path))
            return
        
        # Get the letters that the current digit maps to
        possible_letters = digit_to_char[digits[index]]
        for letter in possible_letters:
            path.append(letter)             # Choose
            backtrack(index + 1, path)      # Explore
            path.pop()                      # Un-choose (backtrack)

    combinations = []
    backtrack(0, [])  # Start backtracking from index 0 with an empty path
    return combinations

# Test the function
result = letter_combinations("232")
print(result)
