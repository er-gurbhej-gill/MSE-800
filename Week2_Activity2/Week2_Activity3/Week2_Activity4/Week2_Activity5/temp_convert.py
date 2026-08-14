class TemperatureConverter:

    def __init__(self, temperature):
        self.temperature = temperature

    def convert(self):
        # Check if input has at least 2 characters
        if len(self.temperature) < 2:
            return "Invalid input. Please enter the temperature with the correct 'C' or 'F' prefix."

        prefix = self.temperature[0]
        value = self.temperature[1:]

        # Check the prefix
        if prefix not in ["C", "F"]:
            return "Invalid input. Please enter the temperature with the correct 'C' or 'F' prefix."

        # Check whether the temperature is a number
        try:
            value = float(value)
        except ValueError:
            return "Invalid input. Please enter the temperature with the correct 'C' or 'F' prefix."

        # Fahrenheit to Celsius
        if prefix == "F":
            celsius = (value - 32) * 5 / 9
            return f"{self.temperature} degrees Fahrenheit is converted to {celsius:.2f} degrees Celsius"

        # Celsius to Fahrenheit
        elif prefix == "C":
            fahrenheit = (value * 9 / 5) + 32
            return f"{self.temperature} degrees Celsius is converted to {fahrenheit:.2f} degrees Fahrenheit"


if __name__ == "__main__":

    user_input = input("Enter temperature (e.g. F51 or C11): ")

    converter = TemperatureConverter(user_input)

    result = converter.convert()

    print(result)