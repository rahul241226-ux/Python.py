
# 8. Property Decorators
# </summary>
# Problem: Use a property decorator in the Car class to make the model attribute read-only.
# </details>










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


      
      @property  #
      def model(self):
            return self.__model


      
      
         
     
#inheritance
class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
          super().__init__(brand,model)
          self.battery_size= battery_size


    def fuel_type(self):
                return " Electric charge"

          


my_tesla = ElectricCar("tesla", "model s","85kw")

my_car = Car("tata","safari")

Car("tata","nexon")

print(my_car.model)

