#3.Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.
 #inheritance 




class Car:
      def __init__(self, userbrand, usermodel):#init is also contrustor
            self.brand = userbrand
            self.model = usermodel 
            


      def full_name(self):  #it add the brand and model of that car.
            return f"{self.brand} {self.model}"

#inheritance
class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
          super().__init__(brand,model)
          self.battery_size= battery_size
          


my_tesla = ElectricCar("tesla", "model s","85kw")
print(my_tesla.model)
print(my_tesla.full_name())
      

# my_car= Car("lambo","corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())



# my_new_car = Car("tata","safari")
# print(my_new_car.brand)
# print(my_new_car.model)