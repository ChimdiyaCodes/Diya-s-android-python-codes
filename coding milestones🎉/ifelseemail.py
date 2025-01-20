def validate_email():
    email = input("Enter your email: ")
    if email and "@" in email:  # Check if email is not empty and contains '@'
        print("Email is valid.")
    else: print("Invalid email. Please enter a valid email address.")

validate_email()
