from app.services.requests.status import code_http, code_message
from app.services.sqlalchemy.pagination import pagination_info


def default_return(status=200, message=2, data={}, items_paginate={}, summary={}):
    """
    It returns a dictionary with the following keys: status, msg, pagination, summary, data
    
    :param status: HTTP status code, defaults to 200 (optional)
    :param message: 2 = "Success", defaults to 2 (optional)
    :param data: The data you want to return
    :param items_paginate: the paginated object
    :param summary: a dictionary of key-value pairs that you want to return
    :return: A tuple of three items:
    1. A dictionary
    2. An integer
    3. A dictionary
    """
    pagination = pagination_info(items_paginate)

    data = {
        "status": code_http(status),
        "msg": code_message(message),
        "pagination": pagination,
        "summary": summary, "data": data
    }

    return data, status, {"Content-Type": "application/json"}
