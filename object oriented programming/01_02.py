#1.Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.



class Car:
      def __init__(self, userbrand, usermodel):#init is also contrustor
            self.brand = userbrand
            self.model = usermodel 
            


#2.Problem: Add a method to the Car class that displays the full name of the car (brand and model).
      def full_name(self):  #it add the brand and model of that car
            return f"{self.brand} {self.model}"

      

my_car= Car("lambo","corolla")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())



my_new_car = Car("tata","safari")
print(my_new_car.brand)
print(my_new_car.model)