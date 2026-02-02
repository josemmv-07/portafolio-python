def main():
    usuario = int(input("Grados Fahreheit: "))
    celsius = (usuario - 32) * 5 / 9
    print(f"La temperaatura en grado Celsius es: {celsius}")

if __name__ == "__main__":
    main()