def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def main():
    print("Welcome to the Temperature Conversion Program!")
    print("Please select the unit of the temperature you want to convert from:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    choice = int(input("Enter your choice (1/2/3): "))

    if choice not in [1, 2, 3]:
        print("Invalid choice! Please select 1, 2, or 3.")
        return

    temperature = float(input("Enter the temperature value: "))

    if choice == 1:  
        converted_fahrenheit = celsius_to_fahrenheit(temperature)
        converted_kelvin = celsius_to_kelvin(temperature)
        print(f"{temperature} degrees Celsius is equal to {converted_fahrenheit:.2f} degrees Fahrenheit.")
        print(f"{temperature} degrees Celsius is equal to {converted_kelvin:.2f} Kelvin.")
    elif choice == 2:  
        converted_celsius = fahrenheit_to_celsius(temperature)
        converted_kelvin = fahrenheit_to_kelvin(temperature)
        print(f"{temperature} degrees Fahrenheit is equal to {converted_celsius:.2f} degrees Celsius.")
        print(f"{temperature} degrees Fahrenheit is equal to {converted_kelvin:.2f} Kelvin.")
    else:  
        converted_celsius = kelvin_to_celsius(temperature)
        converted_fahrenheit = kelvin_to_fahrenheit(temperature)
        print(f"{temperature} Kelvin is equal to {converted_celsius:.2f} degrees Celsius.")
        print(f"{temperature} Kelvin is equal to {converted_fahrenheit:.2f} degrees Fahrenheit.")

if __name__ == "__main__":
    main()
