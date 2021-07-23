class Singleton(type):
    _instances = {}  # dict
    def __call__(cls, *args, **kwargs):  # cls for the first argument to class methods.
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
        
class Logger(metaclass=Singleton):  # metaclass: the class of a class.
    pass

class Other():
    pass

logger1, logger2 = Logger(), Logger()
other1, other2 = Other(), Other()

assert (logger1 is logger2) == True
assert (other1 is other2) == False