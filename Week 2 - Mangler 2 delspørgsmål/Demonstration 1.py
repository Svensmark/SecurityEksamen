import re

def validate_password_strength(password):
    if re.search(r'\d', password):
        print("Has a digit")
    else:
        print("Must contain digit")

    if re.search(r'[A-Z]', password):
        print("Has a lower case letter")
    else:
        print("Must contain upper case letter")

    if re.search(r'[a-z]', password):
        print("Has a lower case letter")
    else:
        print("Must contain lower case letter")

    if len(password) >= 8:
        print("Has a length of 8 or more characters")
    else:
        print("Must have a length of 8 or more characters")
    print("")


validate_password_strength("")
validate_password_strength("1")
validate_password_strength("T1")
validate_password_strength("Test1")
validate_password_strength("Test1....")