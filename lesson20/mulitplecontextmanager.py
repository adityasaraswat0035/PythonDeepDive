import contextlib
@contextlib.contextmanager
def nest_test(name):
    print('Entering', name)
    yield
    print('Exiting', name)

with nest_test('outer'), nest_test('inner'):
    print('BODY')


with nest_test('outer'):
    with nest_test('inner'):
        print('Body')
    
@contextlib.contextmanager
def nest_testV1(name):
    print('Entering', name)
    yield name
    print('Exiting', name)

with nest_testV1('outer') as n1,nest_testV1('inner,nested in '+n1) as n2:
    print(n2)
    print('BODY')


@contextlib.contextmanager
def propagater(name, propagate):
    try:
        yield
        print(name, 'exited normally.')
    except Exception:
        print(name, 'received an exception!')
        if propagate:
            raise

with propagater('outer', True), propagater('inner', False):
    raise TypeError('Cannot convert lead into gold.')

with propagater('outer', False), propagater('inner', True):
    raise TypeError('Cannot convert lead into gold.')

with (nest_test('a'), nest_test('b')): # Error as here it will call __enter__ and __exit__ on tuple not on indivisual so better to pass as value of comma seperated
     pass

with nest_test('a'), \
    nest_test('b'), \
    nest_test('c'):
    pass
