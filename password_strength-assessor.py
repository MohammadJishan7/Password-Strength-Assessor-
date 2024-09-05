import re

def assess_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_character_criteria = re.search(r'[\W_]', password) is not None

    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_character_criteria])
    
    if criteria_met == 5:
        return "Strong"
    elif criteria_met >= 3:
        return "Moderate"
    else:
        return "Weak"

# Example usage
password = input("Enter the password: ")
strength = assess_password_strength(password)
print(f"The strength of the password '{password}' is: {strength}")