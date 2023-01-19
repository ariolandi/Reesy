def type_of(x):
    """
    Determinates the type of the argument.
    If an instance of class type is received, it returns the argument itself.
    In other cases, returns the type of the argument.

    Special cases:
    [T], where T is a valid type, expects a list of type T
    [] expects a list of any type
    (T, S), whete T and S are valid types, expects either T or S 
    """

    def _type(y):
        return y if type(y) is type else type(y)

    if type(x) is list:
        return [type_of(x[0])] if x != [] else []
    elif type(x) is tuple:
        return tuple([type_of(y) for y in x])
    else:
        return _type(x)


def arguments_types(*args, **kwargs):
    """
    Returns a dictionary with all arguments' types
    in the according possitions/keywords.
    """

    types = {position: type_of(x) for position, x in enumerate(args)}
    types.update({key: type_of(x) for (key, x) in kwargs.items()})
    return types


def is_type(actual_type, expected_type):
    """
    Checks if two types are equal.
    Note that a [] as a type is equal with [T] with any type T.
    Note that if the expected type is a tuple, then we expect either
        of the types in the tuple.
    """

    def _equal_list_types(type1, type2):
        return type(type1) is list and type(type2) is list and\
            (not type1 or not type2 or is_type(type1[0], type2[0]))

    def _contains_type(actual_type, expected_type):
        return type(expected_type) is tuple and\
            any([is_type(actual_type, x) for x in expected_type])

    return actual_type == expected_type or\
        _equal_list_types(actual_type, expected_type) or\
        _contains_type(actual_type, expected_type)
