import re

# Password Checker Tool
def check_password(password) :
    comment = str("")

        # Should contain at least 8 Characters
    if len(password) < 8  :
            comment += ("Password Should at least 8 characters !! \n")

        # Should contain at least one uppercase letter
    if not any(char.isupper() for char in password):
          comment += ("Password must contain at least one uppercase letter !! \n")

        # Should contain at least one lowercase letter
    if not any(char.islower() for char in password):
           comment+=("Password must contain at least one lowercase letter !!\n" )

        # Should contain at least one digit
    if not any(char.isdigit() for char in password):
           comment+=("Password must contain at least one digit !!\n")

        # Should contain at least one special character
    special_characters = re.compile(r"[!@#$%^&*(),.?\":{}|<>]")
    if not special_characters.search(password) :
            comment+=("Password must contain at least one special character !!\n")

    else: comment=('Password is Strong (-.-)')

    return print(comment)



#Example
    # User Input
password = input("Please Enter your Password : ")
check_password(password)