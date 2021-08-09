with open('important_data.txt', 'wt') as f:
    f.write('The secret password is 12345')


class LoggingContextManager:
    def __enter__(self):
        return self
    def __exit__(self,exec_type,exec_val,exec_tb):
        return

with LoggingContextManager() as x:
    print(x) #<__main__.LoggingContextManager object at 0x000002711A521E20>

class LoggingContextManagerV2:
    def __enter__(self):
        return "You're in a with-block!"
    def __exit__(self,exc_type,exc_val,exc_tb):
        return
with LoggingContextManagerV2() as y:
    print(y)

class LoggingContextManagerV3:
    def __enter__(self):
        print('LoggingContextManager.__enter__()')
        return "You're in a with-block!"
    def __exit__(self,exc_type,exc_val,exc_tb):
        print('LoggingContextManager.__exit__({}, {}, {})'.format(
            exc_type, exc_val, exc_tb))
        return

with LoggingContextManagerV3() as z:
    print(z)

try:
    with LoggingContextManagerV3() as q:
        print(q)
        raise Exception("Something bad happend")
except Exception as e:
    print(e)

class LoggingContextManagerV4:
    def __enter__(self):
        print('LoggingContextManager.__enter__()')
        return "You're in a with-block!"
    def __exit__(self,exc_type,exc_val,exc_tb):
        if exc_type is None:
            print('LoggingContextManager.__exit__: normal exit detected')
        else:
            print('LoggingContextManager.__exit__: Exception detected! type={}, value={}, traceback={}'.format(exc_type, exc_val, exc_tb))
        return


try:
    with LoggingContextManagerV3() as q:
        print(q)
        raise Exception("Something bad happend")
except Exception as e:
    print(e)