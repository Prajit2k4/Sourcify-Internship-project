def factorial(n):
    """Calculate the factorial of a given number."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    print("Welcome to the Factorial Calculator!\n")

    while True:
        try:
            num = int(input("Please enter a non-negative integer: "))
            if num < 0:
                raise ValueError("Please enter a non-negative integer.")
            else:
                result = factorial(num)
                print(f"\nThe factorial of {num} is: {result}\n")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        restart = input("Do you want to calculate another factorial? (yes/no): ")
        if restart.lower() != "yes":
            print("\nThank you for using the Factorial Calculator. Goodbye!")
            break
        print()

if __name__ == "__main__":
    main()
