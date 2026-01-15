def volume(l=1,b=1,c=1):
    print(f"l={l},b={b},c={c}")
    return l*b*c

v=volume(5,10,2)
print(v)

v=volume(5,10)
print(v)

v=volume(5)
print(v)

v=volume()
print(v)


def func(a="hello",b=13.7,c=36):
    print(a,b,c)

func(5,10,20)
fn=func()


def func(l=[1,2,3]):
    l.append(len(l))
    print(l)

func()
func()
func([10,11])
func()