from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before function runs")
        func()
        print("After functrions runs")
    return wrapper

@my_decorator
def great():
    print('Hello from decorators class from chaicoder')

great()
print(great.__name__)