""" validate strings against regex """
import regex

def validate_pw(inputstr):
    """
    validates a password string
    """
    if len(inputstr) >= 8:
        return True
    return False

def validate_username(inputstr):
    """
    validates a username string

    regex source:
    https://stackoverflow.com/a/46413626
    """
    pattern = r"[\p{L}\p{N}\-\.\_ ]+\Z"
    match = regex.match(pattern, inputstr)
    return match is not None
