import logging
logging.basicConfig(level=logging.INFO)

def logging_deco(func):
    def wrapper(*args, **kwargs):
        logging.info(f"{func.__name__} 호출 시작")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} 호출 끝")
        return result
    return wrapper

@logging_deco
def example_func():
    print("Example function RUN")

example_func()

"""
wrapper 함수에서는
1) func 함수가 호출되기 전과 후에 로그 정보를 출력하고
2) func 함수를 실행한 결과를 반환한다.
"""