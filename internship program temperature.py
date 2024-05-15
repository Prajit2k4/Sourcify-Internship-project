def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def main():
    print("Welcome to the Temperature Converter!\n")

    while True:
        try:
            choice = input("Which conversion would you like to perform?\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\nEnter your choice (1 or 2): ").strip()
            if choice not in ['1', '2']:
                raise ValueError("Invalid choice. Please enter '1' or '2'.")
            else:
                if choice == '1':
                    celsius = float(input("Enter the temperature in Celsius: "))
                    result = celsius_to_fahrenheit(celsius)
                    print(f"The temperature {celsius}°C is equivalent to {result:.2f}°F.\n")
                else:
                    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
                    result = fahrenheit_to_celsius(fahrenheit)
                    print(f"The temperature {fahrenheit}°F is equivalent to {result:.2f}°C.\n")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        restart = input("Would you like to perform another conversion? (yes/no): ")
        if restart.lower() != "yes":
            print("\nThank you for using the Temperature Converter. Goodbye!")
            break
        print()

if __name__ == "__main__":
    main()
