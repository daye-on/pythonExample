def name_func(*Names):
    for name in Names:
        print("%s %s" % (name[0], name[1:3]), end=' ')
    print("\n")
    # type(Names) >>> <class 'tuple'>

name_func('사용자')
name_func('사용자', '성이름')
name_func('사용자', '성이름', '김이름')
name_func('사용자', '성이름', '김이름', '이이름')