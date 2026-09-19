class pizza:
    def prepare(self):
        print("preparing pizza")

class burger:
    def prepare(self):
        print("preparing burger")

class pasta:
    def prepare(self):
        print("preparing pasta")
        
class food_factory:
    def create_food(self, food_type):

        food_type = food_type.lower()

        if food_type == "pizza":
            return pizza()

        elif food_type == "burger":
            return burger()

        elif food_type == "pasta":
            return pasta()

        else:
            return None

food_type = input("enter_food_(pizza/burger/pasta): ")

factory = food_factory()
food = factory.create_food(food_type)

if food is not None:
    food.prepare()
else:
    print("invalid_food_choice")