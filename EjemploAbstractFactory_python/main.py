from cliente import *


def main():
    c = Cliente()
    print("Fábrica Samsung: ")
    c.accion_cliente(CelularSamsungFac())
    print("Fábrica Xiaomi: ")
    c.accion_cliente(CelularXiaomiFac())


if __name__ == "__main__":
    main()