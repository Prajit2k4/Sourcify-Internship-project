def is_prime(num):
    """Check if a given number is a prime number."""
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        # Check divisibility only up to the square root of the number
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

def main():
    print("Welcome to the Prime Number Checker Bot!\n")
    print("I'll help you check for the prime number !\n")

    while True:
        try:
            num = int(input("Please enter a positive integer: "))
            if num <= 0:
                raise ValueError("Please enter a positive integer.")
            else:
                if is_prime(num):
                    print(f"\nThe number {num} is a prime number.\n")
                else:
                    print(f"\nThe number {num} is not a prime number.\n")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        restart = input("Do you want to check another number? (yes/no): ")
        if restart.lower() != "yes":
            print("\nThank you for using the Prime Number Checker. Goodbye!")
            break
        print()

if __name__ == "__main__":
    main()
