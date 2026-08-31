#6. Class Variables
#Problem: Add a class variable to Car that keeps track of the number of cars created.



class Car:
      total_car= 0
      def __init__(self, userbrand, usermodel):#init is also contrustor
            self.__brand = userbrand#if we put tw underscore on any object then it get private 
            self.model = usermodel 
            Car.total_car +=1

            
      def get_brand(self):
            return self.__brand + " ! "

      def full_name(self):  
            return f"{self.__brand} {self.model}"
      

      def fuel_type(self):
            return "petrol or diesel"
     
#inheritance
class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
          super().__init__(brand,model)
          self.battery_size= battery_size


    def fuel_type(self):
                return " Electric charge"
         
          


my_tesla = ElectricCar("tesla", "model s","85kw")
# print(my_tesla.__brand)
print(my_tesla.fuel_type())
safari = Car("tata","safari")
print(safari.fuel_type())

print(Car.total_car)
