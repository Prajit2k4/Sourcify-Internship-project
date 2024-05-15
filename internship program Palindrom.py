def is_palindrome(s):
    """Check if a given string is a palindrome."""
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    # Compare the string with its reverse
    return s == s[::-1]

def main():
    print("     <Palindrome Checker>     \n")
    string = input("Enter the string you want to check: ")

    if is_palindrome(string):
        print("\n     ✨ The entered string is a palindrome! ✨")
    else:
        print("\n     ❌ The entered string is not a palindrome. ❌")

if __name__ == "__main__":
    main()
