from sqlalchemy import func


def dynamic_filters(class_model, query, extra_filters):
    '''
    Return filtered queryset based on condition.
    :param query: takes query
    :param filter_condition: Its a list, ie: [(key,operator,value)]
    operator list:
        eq for ==
        ne for !=
        gt for >
        lt for <
        ge for >=
        le fpr <=
        in for in_
        not_in for not_in
        like for like
        value could be list or a string
    :return: queryset
    '''
    for raw in extra_filters:
        try:
            key, op, value = raw
        except ValueError:
            raise Exception('Invalid filter: %s' % raw)

        if 'date(' in key:
            key = key.replace('date(', '').replace(')', '')
            column = func.date(getattr(class_model, key, None))
        else:
            column = getattr(class_model, key, None)

        if column is None:
            raise Exception('Invalid filter column: %s' % key)

        if op == 'in':
            if isinstance(value, list):
                filt = column.in_(value)
            else:
                filt = column.in_(value.split(','))
        elif op == 'not_in':
            if isinstance(value, list):
                filt = column.not_in(value)
            else:
                filt = column.not_in(value.split(','))
        else:
            try:
                attr = list(filter(
                    lambda e: hasattr(column, e % op),
                    ['%s', '%s_', '__%s__']
                ))[0] % op
            except IndexError:
                raise Exception('Invalid filter operator: %s' % op)
            if value == 'null':
                value = None
            filt = getattr(column, attr)(value)

        query = query.filter(filt)

    return query
