import base64
from mimetypes import guess_extension, guess_type


def get_base64_image(file):
    """
    It takes a base64 encoded image, decodes it, and returns the image and the extension of the image
    
    :param file: The base64 encoded image
    :return: The image and the extension of the image.
    """
    file_exp = file.split(',')
    image = base64.b64decode(file_exp[1])
    ext = guess_extension(guess_type(file)[0])

    return image, ext