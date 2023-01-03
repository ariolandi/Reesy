def filter_list(func, ls):
    return list(filter(func, ls))


def filter_dict(func, dct):
    return {key: value for (key, value) in dct.items() if func(value)}


def flatten(ls):
    import numpy
    return [x.item() for x in numpy.concatenate(ls)]


def count_values(ls):
    from collections import Counter
    return Counter(ls)
