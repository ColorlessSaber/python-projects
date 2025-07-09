"""
An example of OOP Polymorphism
"""

class MathFunctions:
    def multiplication(self, num1, num2):
        return num1 * num2

    def power_to(self, num, power):
        return num**power


class ModifiedMultiplication(MathFunctions):
    def multiplication(self, num1, num2):
        """
        Override MathFunction's method and don't use the built-in function of multiplication
        """
        result = 0
        for i in range(0, num2):
            result += num1
        return result

class ModifiedPower(MathFunctions):
    def power_to(self, num, power):
        """
        Override MathFunction's method and don't use the built-in function of power-to
        """
        result = num
        for i in range(0, power-1): # minus one is so we get the correct multiplication to match power-to
            result *= num
        return result

if __name__ == '__main__':
    mod_multi = ModifiedMultiplication()
    print(mod_multi.multiplication(3,4))

    mod_power = ModifiedPower()
    print(mod_power.power_to(3,2))