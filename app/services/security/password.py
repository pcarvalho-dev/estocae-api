from passlib.handlers.pbkdf2 import pbkdf2_sha256


def get_password_hash(password):
    """
    It takes a password, hashes it, and then stores the hash in the database

    :param password: The password to be hashed
    """
    password = pbkdf2_sha256.hash(password)

    return password


def verify_password(hashed_password, candidate):
    """
    It takes a candidate password and compares it to the stored password

    :param candidate: The password that the user is trying to log in with
    :return: The password is being returned.
    """
    return pbkdf2_sha256.verify(candidate, hashed_password)
