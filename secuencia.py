

def a():
    a = 1
    b()


def b():
    b = 1
    c()


def c():
    c = a + b
    d()


def d():
    d = c + b
    main()


def main():
    a()

if __name__ == "__main__":
    main()
