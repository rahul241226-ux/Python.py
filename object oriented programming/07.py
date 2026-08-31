#static object 

#Problem: Add a static method to the Car class that returns a general description of a car.




class Car:
      total_car= 0
      def __init__(self, userbrand, usermodel):#init is also contrustor
            self.__brand = userbrand#if we put tw underscore on any object then it get private 
            self.__model = usermodel 
            Car.total_car +=1

            
      def get_brand(self):
            return self.__brand + " ! "

      def full_name(self):  
            return f"{self.__brand} {self.__model}"
      

      def fuel_type(self):
            return "petrol or diesel"
#static method(decorator): when we use static method then we does not need to use "self"

      @staticmethod
      def general_description():
           return "Cars are means of transportation"

      
    
      
      
         
     
#inheritance
class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
          super().__init__(brand,model)
          self.battery_size= battery_size


    def fuel_type(self):
                return " Electric charge"

          


my_tesla = ElectricCar("tesla", "model s","85kw")
# print(my_tesla.__brand)
# print(my_tesla.fuel_type())
my_car = Car("tata","safari")
my_car.model="city"
Car("tata","nexon")
# print(my_car.general_description())
# print(Car.general_description())
print(my_car.model)

# print(Car.total_car)
