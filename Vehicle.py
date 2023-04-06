#Vehicle Class

#Constructor = __init__ have parameters make model year

#Class level funcion called start(self)   stop(self)
# start(self) print out The vehicle is starting ...
# stop(self) print out The vehicle is stopping ...


#3 instances of the Vehicle class
# 1 blue_car - Ford Mach-E 2021
# 2 red_car - Tesla Model X 2022
# 3 black_car - Chevy Bolt 2020
# start and stop each car





class Vehicle: #Class is the blueprint of what it could be
    doors = 4 #This will assign to all the objects, it lives in all of them when like this. AKA Class level attribute/parameter/argument


    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print('The', self.year, self.make, 'is starting ...')
    def stop(self):
        print('The', self.make, ' is stopping ...')
    def print_details(self):
        print('The', self.make, 'has', self.doors, 'doors')





#Assigning the cars make model and year
blue_car = Vehicle('Ford', 'Mach-E', 2021)  #These are objects, they are instance of the Vehicle class
red_car = Vehicle('Tesla', 'Model X', 2022)
black_car = Vehicle('Chevy', 'Bolt', 2020)

blue_car.start()
blue_car.stop()
blue_car.print_details()
red_car.start()
red_car.stop()

black_car.start()
black_car.stop()
