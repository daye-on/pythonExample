def permission_deco(permission):
    def decorator(func):
        def wrapper(*args, **kwargs):
            user_permission = ['read', 'write']
            if permission in user_permission:
                return func(*args, **kwargs)
            else:
                raise Exception('Permission error')

        return wrapper
    return decorator

"""
permission_deco 함수는 권한이 있는 사용자만 함수를 실행할 수 있도록 하는 데코레이터를 반환한다.
permission으로 사용자의 권한을 확인하고, func 함수를 실행하거나 예외를 발생시킨다.
"""

@permission_deco('read')
def read():
    print("읽기 함수 실행")

@permission_deco('delete')
def delete():
    print("삭제 함수 실행")

try:
    read()
    delete()
except Exception as e:
    print(e)