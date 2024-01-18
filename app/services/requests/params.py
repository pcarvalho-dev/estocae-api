from flask import request


def custom_parameters():
    """
    It returns the values of the query parameters `page`, `per_page`, `search`, `order`, and `order_by`
    as integers, strings, or `None` if they are not present
    :return: A tuple of the values of the parameters.
    """
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=12, type=int)
    search = request.args.get('search')
    order = request.args.get('order', default='name')
    order_by = request.args.get('order_by', default='asc')

    return page, per_page, search, order, order_by