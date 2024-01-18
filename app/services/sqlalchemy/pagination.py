def pagination_info(pagination_result):
    """
    It returns a dictionary with the pagination info.
    
    :param pagination_result: The pagination result object
    :return: A dictionary with the following keys:
    """
    """Return pagination info"""

    try:
        info = {
            "has_next": pagination_result.has_next,
            "has_prev": pagination_result.has_prev,
            "current_page": pagination_result.page,
            "total_items": pagination_result.total,
            "total_pages": pagination_result.pages
        }
    except:
        info = {}

    return info
