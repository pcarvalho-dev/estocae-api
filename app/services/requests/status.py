def code_message(message_or_code):
    """
    If the message_or_code is a number, return the corresponding message. Otherwise, return the
    message_or_code.
    
    :param message_or_code: The message or code that you want to be translated
    :return: The message is being returned.
    """
    if message_or_code == 1:
        message = "Registered successfully"
    elif message_or_code == 2:
        message = "Query made successfully"
    elif message_or_code == 3:
        message = "Updated successfully"
    elif message_or_code == 4:
        message = "Deleted successfully"
    elif message_or_code == 5:
        message = "Missing field"
    elif message_or_code == 6:
        message = "Not Found"
    elif message_or_code == 7:
        message = "Already registered"
    elif message_or_code == 8:
        message = "Already Deleted"
    elif message_or_code == 9:
        message = "Status change not permitted. The data was not updated"
    else:
        message = message_or_code

    return message


def code_http(code):
    """
    If the code is 200, the status is OK. If the code is 201, the status is Created. If the code is 206,
    the status is Partial Content. If the code is 302, the status is Found. If the code is 400, the
    status is Bad Request. If the code is 401, the status is Unauthorized. If the code is 402, the
    status is Payment Unauthorized. If the code is 403, the status is Forbidden. If the code is 404, the
    status is Not Found. If the code is 405, the status is Method Not Allowed. If the code is 406, the
    status is Not Acceptable. If the code is 409, the status is Conflict. If the code is 415, the status
    is Unsupported Media Type. If the code is 429, the status is Too Many Request. If the code is 500,
    the status is Internal Server Error. If the code is 503, the status is Service Unavailable
    
    :param code: The HTTP status code
    :return: The status of the code.
    """
    if code == 200:
        status = "OK"
    if code == 201:
        status = "Created"
    if code == 204:
        status = "No Content"
    if code == 206:
        status = "Partial Content"
    if code == 302:
        status = "Found"
    if code == 400:
        status = "Bad Request"
    if code == 401:
        status = "Unauthorized"
    if code == 402:
        status = "Payment Unauthorized"
    if code == 403:
        status = "Forbidden"
    if code == 404:
        status = "Not Found"
    if code == 405:
        status = "Method Not Allowed"
    if code == 406:
        status = "Not Acceptable"
    if code == 409:
        status = "Conflict"
    if code == 415:
        status = "Unsupported Media Type"
    if code == 429:
        status = "Too Many Request"
    if code == 500:
        status = "Internal Server Error"
    if code == 503:
        status = "Service Unavailable"

    return status
