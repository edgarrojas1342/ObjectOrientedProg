# Class is the blueprint of OOP
class Person:
    #Class level attributes
    #Initializer or constructor
    #Self is used in python, other languages may use --> this
    def __init__(self,name, age, eye_color):
        self.name = name
        self.age = age
        self.eye = eye_color

    def print_person_info(self):
        print (self.name, 'age is', self.age, 'eye color is', self.eye)




# outside of the class
#Object
edgar = Person('Edgar', 26, 'Black') #Edgar is an instance of the Person class
lexi = Person('Lexi', 26, 'Blue') #Lexi is an instance of the Person class
sally = Person('Sally', 39, 'brown')
greg = Person('Greg', 60, 'Green')

#Assign attributes to an object using the . operator

edgar.print_person_info()
lexi.print_person_info()
sally.print_person_info()
greg.print_person_info()






