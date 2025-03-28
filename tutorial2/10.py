import re
def is_valid_password(pwd):
    if (len(pwd) >= 6 and
        re.search("[a-zA-Z]", pwd) and
        re.search("[0-9]", pwd) and
        re.search("[$#@]", pwd)):
        return "Valid Password"
    return "Invalid Password"
print(is_valid_password("Passw0rd@"))