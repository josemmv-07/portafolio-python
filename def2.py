from time import sleep

def c():
    print("C")
    sleep(1)
    a()


def b():
    print("B")
    sleep(1)
    c()


def a():
    print("A")
    sleep(1)
    b()


def main():
    a()


if __name__ == "__main__":
    main()