def func(a,b,*,c,d):
    print(a,b,c,d)

func(6,b=12,c=13,d=14)


def func(*,a,b,c,d):
    print(a,b,c,d)
func(a=1,b=2,c=3,d=4)
