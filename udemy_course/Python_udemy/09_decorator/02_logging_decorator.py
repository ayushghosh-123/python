from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwergs):
        print(f'calling {func.__name__}')
        result = func(*args , **kwergs)
        print(f'Finished: {func.__name__}')
        return result
    return wrapper

@log_activity
def brew_chai(type, milk='no'):
    print(f'Brewing {type} chai with milk status: {milk}')

brew_chai("Masala")