def timeit(func):
    from time import time

    def wrapper(*args, **kwargs):
        start = time()
        ans = func(*args, **kwargs)
        print(f'Executed in {time() - start: .3f} ms')
        return ans
    return wrapper
