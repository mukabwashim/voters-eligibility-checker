def check_voter_eligibility():
    # Get user input
    citizenship = input("Enter your citizenship (e.g., Kenya, Uganda, Tanzania): ").strip().lower()
    
    # Check if the user is a citizen of an eastern African country
    if citizenship not in ['kenya', 'uganda', 'tanzania']:
        print("Sorry, you are not eligible to vote. You must be a citizen of Kenya, Uganda, or Tanzania.")
        return

    # Get user age
    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("Invalid age input. Please enter a valid number.")
        return
    
    # Check if the user is 18 years of age or older
    if age < 18:
        print("Sorry, you are not eligible to vote. You must be 18 years of age or older.")
        return

    # Ask if the user has a valid ID
    has_valid_id = input("Do you have a valid ID? (yes/no): ").strip().lower()

    # Check if the user has a valid ID
    if has_valid_id != 'yes':
        print("Sorry, you are not eligible to vote. You must have a valid ID.")
        return

    # If all conditions are met, the user is eligible to vote
    print("Congratulations! You are eligible to vote.")

# Run the function to check eligibility
check_voter_eligibility()
