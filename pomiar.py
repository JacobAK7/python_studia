from time import time

def timer_func(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        message = f'Wykonano funkcje: {func.__name__} w czasie: {(t2 - t1):.4f}s'
        print(message)
        return result

    return wrap_func

if __name__ == "__main__":
    print ("Pomiar is being run directly")

    @timer_func
    def long_time(n):
        for i in range(n):
            for j in range(100000):
                i * j

    long_time(100)

else:
    print ("Pomiar is being imported")