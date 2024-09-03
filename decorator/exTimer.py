import time

def timer_deco(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"실행 시간: {end_time - start_time:.3f} seconds")
        return result
    return wrapper

@timer_deco
def example_func():
    time.sleep(1)

example_func()

"""
timer_deco 함수는 함수를 인자로 받아
해당 함수를 실행 하는데 걸리는 시간을 측정하여 출력하는 함수이다.
"""