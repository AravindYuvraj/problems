def get_valid_input(prompt):
    while True:
        user_input = input(prompt)

        # Check if input is empty
        if user_input.strip() == "":
            print("Input cannot be empty. Please try again.")
            continue
        
        try:
            # Try to convert to integer
            value = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        # Check if input is in the allowed range
        if value < 1 or value > 120:
            print(f"Input must be between 1 and 120.")
            continue

        # If everything is valid, return the value
        return value

# Example usage
number = get_valid_input("Enter your age :(1-120) ")
print(f"Thanks! You entered age is : {number}")
