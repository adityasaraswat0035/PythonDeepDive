"""
@contextlib.contextmanager
def my_context_manager():
# <ENTER>
try:
yield [value]
# <NORMAL EXIT>
except:
# <EXCEPTIONAL EXIT>
raise
"""

import contextlib
import sys
from typing import ContextManager

@contextlib.contextmanager
def logging_context_manager():
    print("Logging context manager: enter")
    try:
        yield "You're in a with block"
        print("Logging context manager: normal exit")
    except Exception:
        print("Logging context manager : exectional exit can raise exception here",sys.exc_info())


with logging_context_manager() as x:
    print(x)


@contextlib.contextmanager
def logging_context_managerV2():
    print("Logging context manager: enter")
    try:
        yield "You're in a with block"
        print("Logging context manager: normal exit")
    except Exception:
        print("Logging context manager : exectional exit can raise exception here",sys.exc_info())
    

try:
    with logging_context_managerV2() as y:
        print(y)
        raise ValueError("this is not a correct value")
    print("Post Value Error")    
except ValueError:
    print("Inside Value Error")

@contextlib.contextmanager
def logging_context_managerV3():
    print("Logging context manager: enter")
    try:
        yield "You're in a with block"
        print("Logging context manager: normal exit")
    except Exception:
        print("Logging context manager : exectional exit can raise exception here",sys.exc_info())
        raise
    

try:
    with logging_context_managerV3() as y:
        print(y)
        raise ValueError("this is not a correct value")
    print("Post Value Error")    
except Exception as e:
    print("Inside Value Error",str(e))