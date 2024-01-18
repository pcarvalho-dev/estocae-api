import random


def get_promo_code(num_chars):
    """
    It generates a random promo code.
    
    :param num_chars: The number of characters in the promo code
    :return: A string of random characters.
    """
    code_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    code = ""
    for i in range(0, num_chars):
        slice_start = random.randint(0, len(code_chars) - 1)
        code += code_chars[slice_start: slice_start + 1]
    return code
