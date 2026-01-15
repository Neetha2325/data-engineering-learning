def greetings():
    print("Hello !")

def greetings2(name):
    print(f"hello ,{name} !")

greetings()
greetings2("Neetha")


def volume(l,b,h):
    return l*b*h

if __name__=="__main__":
    v=volume(10,10,10)
    print(v)