class Calculadora:
    
    def sumar(self, num1, num2):
        return num1 + num2

    def restar(self, num1, num2):
        return num1 - num2

    def multiplicar(self, num1, num2):
        return num1 * num2

    def dividir(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("No se puede dividir entre cero")


