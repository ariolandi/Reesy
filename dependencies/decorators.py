from .decorators_utils import arguments_types, is_type


def verify_types(*args, **kwargs):
    expected_types = arguments_types(*args, **kwargs)

    def decorator(func):
        def verify(*args, **kwargs):
            actual_types = arguments_types(*args, **kwargs)
            for position in actual_types.keys():
                if position in expected_types.keys() and\
                    not is_type(actual_types[position], expected_types[position]):
                    raise TypeError(
                        f'Argument {position} should be type {expected_types[position]}'
                    )
            return func(*args, **kwargs)
        return verify

    return decorator


def upper(func):
    def decorator(*args, **kwargs):
        args = [x.upper() if type(x) == str else x for x in args]
        kwargs = {k: (x.upper() if type(x) == str else x)
                  for k, x in enumerate(kwargs)}
        return func(*args, **kwargs)
    return decorator
