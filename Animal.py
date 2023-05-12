class Animal: #Parent Class
    def speak(self): #Parent Function
        print('The animal makes a sound')

class Dog(Animal):
    def speak(self): #Override the parent class (New thing)
        print ('Bork Bork')

animal = Animal()
fido = Dog()

animal.speak()
fido.speak()