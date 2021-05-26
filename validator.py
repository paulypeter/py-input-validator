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
    """
    pattern = r"[0-9a-zA-ZäöüßÄÖÜẞ\-_]+\Z"
    match = regex.match(pattern, inputstr)
    return match is not None
