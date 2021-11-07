class Motor:
    def saluda(self):
        pass

class Ruedas:
    def saluda(self):
        pass

class MotorHonda(Motor):
    def saluda(self):
        print("Tengo motor honda")

class MotorToyota(Motor):
    def saluda(self):
        print("Tengo motor Toyota")

class MotorBmw(Motor):
    def saluda(self):
        print("Tengo motor BMW")

class RuedasBridgestone(Ruedas):
    def saluda(self):
        print("Tengo ruedas Bridgestone")

class RuedasPirelli(Ruedas):
    def saluda(self):
        print("Tengo ruedas Pirelli")

class RuedasGoodyear(Ruedas):
    def saluda(self):
        print("Tengo ruedas Goodyear")

class Auto:
    def __init__(self, motor: Motor, ruedas: Ruedas):
        self.motor = motor
        self.ruedas = ruedas

    def datos(self):
        self.motor.saluda()
        self.ruedas.saluda()

motor_honda = MotorHonda()
ruedas_goodyear = RuedasGoodyear()

auto1 = Auto(motor_honda, ruedas_goodyear)

auto1.datos()


