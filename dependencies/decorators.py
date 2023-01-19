from .decorators_utils import arguments_types, is_type


def verify_types(*args, **kwargs):
    """
    Function decorator.
    Validates if function's arguments are the exact types.
    Raises a type error if there is difference in the types.
    """

    expected_types = arguments_types(*args, **kwargs)

    def verify(func):
        def decorator(*args, **kwargs):
            actual_types = arguments_types(*args, **kwargs)
            for position in actual_types.keys():
                if position in expected_types.keys() and\
                    not is_type(actual_types[position],
                                expected_types[position]):
                    raise TypeError(f'Argument {position} should be type\
 {expected_types[position]} instead of {actual_types[position]}')
            return func(*args, **kwargs)
        return decorator

    return verify


def upper(func):
    """
    Function decorator.
    Transforms all strings in the arguments to upper case.
    """

    def decorator(*args, **kwargs):
        args = [x.upper() if type(x) == str else x for x in args]
        kwargs = {k: (x.upper() if type(x) == str else x)
                  for k, x in enumerate(kwargs)}
        return func(*args, **kwargs)
    return decorator


def verify_only_symbol(func):
    """
    Function decorator.
    Validates that all strings in the arguments are only containing one symbol.
    Raises a value error in other case.
    """

    def decorator(*args, **kwargs):
        arguments = list(args)
        arguments.extend(list(kwargs.values()))
        if not all([(len(x) == 1) for x in arguments if type(x) == str]):
            raise ValueError('Only one symbol strings are expected')
        return func(*args, **kwargs)
    return decorator
