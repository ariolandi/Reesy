def filter_list(func, ls):
    return list(filter(func, ls))


def filter_dict(func, dct):
    return {key: value for (key, value) in dct.items() if func(value)}


def flatten(ls):
    return [x for xs in ls for x in xs]


def join(ls):
    ls = filter_list(lambda x: x, ls)
    return [y for x in ls for y in x]


def count_values(ls):
    from collections import Counter
    return Counter(ls)


def unique(ls):
    return [x for (i, x) in enumerate(ls) if x not in ls[:i]]


def flatten_sets(ls):
    return [x for (i, x) in enumerate(ls) if
            not any(x.issubset(y) for y in ls[:i])]


def equalize_frequences(frequence_table, control_set):
    offset = max(frequence_table.values()) / max(control_set.values())
    return {key: (value / offset) for key, value in frequence_table.items()}
