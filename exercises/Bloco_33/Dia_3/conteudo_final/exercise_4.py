from exercise_3 import validate_email


def emails_to_validate(arr):
    new_email_list = []
    for email in arr:
        try:
            validate_email(email)
            new_email_list.append(email)
        except ValueError as V:
            print(V)
            pass

    return new_email_list
