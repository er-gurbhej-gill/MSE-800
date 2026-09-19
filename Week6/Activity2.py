def add sprinkles(func):
    def wrapper():
        print("Sprinkles added")
        func()
    return wrapper

@decor 

def get_icecream():
    print("Got Icecream")

get_icecream()

if __name__ == "__main__":
    main()