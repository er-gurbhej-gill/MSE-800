def add_sprinkles(func):
    def wrapper():
        print("Sprinkles added")
        func()

    return wrapper


@add_sprinkles
def get_icecream():
    print("Got Icecream")

if __name__ == "__main__":
    get_icecream()