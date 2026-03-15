def volume(l,b,h):
    print(f"l={l},b={b},h={h}")
    return l*b*h

v=volume(10,2,5)
print(v)

v=volume(l=10,h=5,b=2)
print(v)

v=volume(10,b=2,h=5)
print(v)
