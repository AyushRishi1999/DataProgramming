def is_valid_password(userPass):
    if len(userPass) < 8:
        return False
    if not userPass.isalnum():
        return False
    digit_count = sum(c.isdigit() for c in userPass)
    if digit_count < 2:
        return False
    return True
userPass = input("Enter a password: ")
if is_valid_password(userPass):
    print("Valid password!")
else:
    print("Invalid password. Please follow the password rules.")
