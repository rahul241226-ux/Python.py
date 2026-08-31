#4. Encapsulation

#Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.


class Car:
      def __init__(self, userbrand, usermodel):#init is also contrustor
            self.__brand = userbrand#if we put tw underscore on any object then it get private 
            self.model = usermodel 
            
      def get_brand(self):
            return self.__brand + " ! "

      def full_name(self):  #it add the brand and model of that car.
            return f"{self.__brand} {self.model}"

#inheritance
class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
          super().__init__(brand,model)
          self.battery_size= battery_size
          


my_tesla = ElectricCar("tesla", "model s","85kw")
# print(my_tesla.__brand)
print(my_tesla.get_brand())
