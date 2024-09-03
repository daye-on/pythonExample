def limit_calls_deco(max):
    def decorator(func):
        calls = 0

        def wrapper(*args, **kwargs):
            nonlocal calls
            if calls < max:
                calls += 1
                return func(*args, **kwargs)
            else:
                raise Exception("Max limit exceeded")
        return wrapper
    return decorator

"""
limit_calls_deco 함수는 호출 횟수를 제한하는 '데코레이터'를 반환하는 함수이다.
decorator 함수에서는 calls 변수를 사용하여 횟수를 세고,
max 보다 작은 경우에만 func 함수를 실행하고 calls 변수를 증가시킨다.
max 보다 큰 경우에는 예외를 발생시킨다.
"""

@limit_calls_deco(3)
def example_func():
    print("Run")

for i in range(5):
    try:
        example_func()
    except Exception as e:
        print(e)

"""
example_func 함수에서 데코레이터를 적용하여 실행하면, 최대 3번까지 실행할 수 있다.
for 루프에서 5번 호출하지만, 3번의 호출이 정상적으로 실행되고,
그 이후 2번은 예외가 발생하므로, 예외 메시지를 출력한다.
"""