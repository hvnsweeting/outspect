'''
Better inspect functions - handy for interactive discover new lib/modules

Conventions: all returns objs must have _objs suffix
'''
import inspect


def attrs(obj):
    return [attr for attr in dir(obj) if not attr.startswith('__')]


def attr_objs(obj):
    return [getattr(obj, attr) for attr in dir(obj)]


def public_attrs(obj):
    '''Public attribute names'''
    return [attr for attr in dir(obj) if not attr.startswith('_')]


def pub(obj):
    '''Alias for public_attrs'''
    return public_attrs(obj)


def priv(obj):
    '''Privates attribute names'''
    return [attr for attr in dir(obj) if attr.startswith('_')]


def function_objs(obj):
    return [attr for attr in attr_objs(obj) if inspect.isroutine(attr)]


def functions(obj):
    '''Get funtions names'''
    return [f.__name__ for f in function_objs(obj)]


def classes(obj):
    return [c.__name__ for c in attr_objs(obj) if inspect.isclass(c)]


def public_functions(obj):
    return [f for f in functions(obj) if not f.startswith('_')]


def pub_funcs(obj):
    '''Alias for public_functions'''
    return public_functions(obj)


def modules(obj):
    '''Sub-modules name'''
    return [attr.__name__ for attr in attr_objs(obj) if inspect.ismodule(attr)]


def constants(obj):
    '''CONSTANT attributes of given obj'''
    return [attr for attr in dir(obj) if attr.isupper()]


def to_items(names, obj):
    '''List of name-value from given attribute names and object'''
    return [(attr, getattr(obj, attr)) for attr in names]


def to_objs(names, obj):
    return [getattr(obj, attr) for attr in names]


def test():
    import os
    obj = os
    print(attrs(obj))
    print(public_attrs(obj))
    print(functions(obj))
    print(constants(obj))


if __name__ == "__main__":
    test()
