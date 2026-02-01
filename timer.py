import time

def timer_func(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Wykonano funkcje: {func.__name__} w czasie: {(t2-t1):.4f}s')
        return result
    return wrap_func