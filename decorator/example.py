"""
my_deco 는 데코레이터 함수로
hello 함수를 인자로 받아, wrapper 함수를 반환한다.
@ 기호를 이용하면 간단하고 직관적으로 코드를 작성할 수 있다.
"""

# def my_deco(func):
#     def wrapper():
#         print("--------------")
#         func()
#         print("--------------")
#     return wrapper
#
# def hello():
#     print("안녕하세요.")
#
# deco = my_deco(hello)
# deco()

def my_deco(func):
    def wrapper():
        print("--------------")
        func()
        print("--------------")
    return wrapper

@my_deco
def hello():
    print("안녕하세요.")

hello()