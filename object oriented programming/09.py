
#9. Class Inheritance and isinstance() Function
#Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.






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

          
#09.py

my_tesla = ElectricCar("tesla", "model s","85kw")

print(isinstance(my_tesla,Car))
print(isinstance(my_tesla,ElectricCar))
