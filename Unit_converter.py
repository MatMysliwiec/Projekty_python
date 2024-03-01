class UnitConverter:
    def temperature_converter(self):
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit")

    def currency_converter(self):
        usd_amount = float(input("Enter amount in USD: "))
        exchange_rate = float(input("Enter the exchange rate (USD to EUR): "))
        eur_amount = usd_amount * exchange_rate
        print(f"{usd_amount} USD is equal to {eur_amount} EUR")

    def volume_converter(self):
        liters = float(input("Enter volume in liters: "))
        gallons = liters * 0.264172
        print(f"{liters} Liters is equal to {gallons} Gallons")

    def mass_converter(self):
        kilograms = float(input("Enter mass in kilograms: "))
        pounds = kilograms * 2.20462
        print(f"{kilograms} Kilograms is equal to {pounds} Pounds")

    def length_converter(self):
        meters = float(input("Enter length in meters: "))
        feet = meters * 3.28084
        print(f"{meters} Meters is equal to {feet} Feet")

    # Add more conversion methods as needed...

def main():
    unit_converter = UnitConverter()

    print("1. Temperature Converter")
    print("2. Currency Converter")
    print("3. Volume Converter")
    print("4. Mass Converter")
    print("5. Length Converter")

    choice = int(input("Select the type of converter (1-5): "))

    if choice == 1:
        unit_converter.temperature_converter()
    elif choice == 2:
        unit_converter.currency_converter()
    elif choice == 3:
        unit_converter.volume_converter()
    elif choice == 4:
        unit_converter.mass_converter()
    elif choice == 5:
        unit_converter.length_converter()
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()