class Vehicle:
    def __init__(self,color,price,maximum_speed):
        self.color = color
        self.price = price
        self.maximum_speed = maximum_speed
     

class Car(Vehicle):
    def __init__(self,color,price,maximum_speed,number_tires):
        super().__init__(color, price, maximum_speed)#as we used another constructor here the constructor used in the vehicle gets overwritten, so in order to use it we are using 'super()'
        self.number_tires = number_tires
    def show_details(self):
        print(f"A {self.color} car with a maximum speed of {self.maximum_speed}km/h is priced at {self.price} with {self.number_tires} tires")

result = Car("red", 500000, 200, 4)#giving the values
result.show_details()#calling the function to show the details