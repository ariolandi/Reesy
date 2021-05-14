def filter_list(func, ls):
    return list(filter(func, ls))


def filter_dict(func, dct):
    filtered = list(filter((lambda y: func(y[1])), dct.items()))
    return {key: value for (key, value) in filtered}


def filter_dict_keys(func, dct):
    return list(filter_dict(func, dct).keys())


def flatten(ls):
    import numpy
    return [x.item() for x in numpy.concatenate(ls)]


def count_values(ls):
    from collections import Counter
    return Counter(ls)
