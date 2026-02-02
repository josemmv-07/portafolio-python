from time import sleep

def sumar_uno(a):
    print(a)
    a += 1
    if a != 100:
        sumar_uno(a)


def main():
    sumar_uno(1)

if __name__ == "__main__":
    main()