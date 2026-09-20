class car:
    def get_description(self):
        return "basic_car"
    
    def get_price(self):
        return 2000
    
class car_decorator:
    def __init__(self, car):
        self.car = car

    def get_description(self):
        return self.car.get_description()
    
    def get_price(self):
        return self.car.get_price()
    
class gps(car_decorator):
    def get_description(self):
        return self.car.get_description() + ", gps"
    
    def get_price(self):
        return self.car.get_price() + 500
    
class sunroof(car_decorator):
    def get_description(self):
        return self.car.get_description() + ", sunroof"
    
    def get_price(self):
        return self.car.get_price() + 1000
    
class leather_seats(car_decorator):
    def get_description(self):
        return self.car.get_description() + ", leather_seats"
    
    def get_price(self):
        return self.car.get_price() + 1500
    
class premium_sound(car_decorator):
    def get_description(self):
        return self.car.get_description() + ", premium_sound"
    
    def get_price(self):
        return self.car.get_price() + 800
    
my_car = car()

my_car = gps(my_car)
my_car = sunroof(my_car)
my_car = leather_seats(my_car)

print("car:", my_car.get_description())
print("price: $", my_car.get_price())