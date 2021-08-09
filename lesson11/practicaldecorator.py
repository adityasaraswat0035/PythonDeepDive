# A decorator factory: it returns decorators
def check_non_negative(index):
    # This is the actual decorator
    def validator(f):
        # This is the wrapper function
        def wrap(*args):
            if args[index] < 0:
                raise ValueError('Argument {} must be non-negative.'.format(index))
            return f(*args)
        return wrap
    return validator


@check_non_negative(1)
def create_list(value, size):
    return [value] * size
