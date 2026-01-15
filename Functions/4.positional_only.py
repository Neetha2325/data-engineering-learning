def func(a,b,/,c,d):
    print(a,b,c,d)

func(5,6,7,d=8)


def func(a,b,c,d,/):
    print(a,b,c,d)

func(5,6,7,8)