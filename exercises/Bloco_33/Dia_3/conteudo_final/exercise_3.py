import re


def validate_email(email):
    regex = '^[A-Za-z][a-zA-Z0-9_-]+@[a-zA-Z0-9]+[.][a-z]{3}$'

    if (re.search(regex, email)):
        return None
    else:
        raise ValueError('Invalid email')
