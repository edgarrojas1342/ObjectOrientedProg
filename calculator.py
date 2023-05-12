class Calculator:

    #Polymorphism method overloading
    def add(self, num1, num2, num3=None):
        if num3:
            return num1 + num2 + num3
        else:
            return num1 + num2

sum = Calculator()

print (sum.add(1,2))
print (sum.add(1,2,3))