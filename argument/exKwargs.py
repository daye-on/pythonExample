def my_func(**kwargs):
    for key, value in kwargs.items():
        print("{0} is {1}".format(key, value))

my_func(Myname='dayeon!')

def key_world_func(**kwargs):
    for key, value in kwargs.items():
        if 'ant' in kwargs.keys():
            print("안녕하세요! 개미에요!")
        else:
            print("{0} is {1}".format(key, value))

key_world_func(ant='asdf')