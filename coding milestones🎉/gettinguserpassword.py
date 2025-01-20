#Get the password from the user
password = input("Enter your password: ")
#Ask the user to re-enter the password for confirmation
confirm_password = input("Re-enter your password to confirm: ")
#While the passwords do not match, keep asking for confirmation
while password != confirm_password:
    print("Passwords do not match. Please try again.")
    password = input("Enter your password: ")
    confirm_password = input("Re-enter your password to confirm: ")
#If the passwords match, grant access
print("ACCESS GRANTED!")
