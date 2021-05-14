def type_of(x):
    """
    Determinates the type of the argument.
    If an instance of class type is received, it returns the argument itself.
    In other cases, returns the type of the argument.

    Special cases:
    [T], where T is a valid type, expects a list of type T
    [] expects a list of any type
    """

    def _type(y):
        return y if type(y) is type else type(y)

    if type(x) is list:
        return [_type(x[0])] if x != [] else []
    else:
        return _type(x)


def arguments_types(*args, **kwargs):
    types = {position: type_of(x) for position, x in enumerate(args)}
    types.update({key: type_of(x) for (key, x) in kwargs.items()})
    return types


def is_type(actual_type, expected_type):
    def _equal_list_types(type1, type2):
        return type(type1) is list and type(type2) is list and\
            (not type1 or not type2 or type1[0] == type2[0])

    return actual_type == expected_type or\
        _equal_list_types(actual_type, expected_type)
