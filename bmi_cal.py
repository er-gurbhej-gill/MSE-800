class bmi:
    def calculate_bmi():
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in metres: "))
        bmi = weight / (height ** 2)
        print("Your BMI is:", round(bmi, 2))

if __name__ == "__main__":
    bmi.calculate_bmi()