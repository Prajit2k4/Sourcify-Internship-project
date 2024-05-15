class Book:
    def __init__(self, code, title, author, quantity):
        self.code = code
        self.title = title
        self.author = author
        self.quantity = quantity

    def __str__(self):
        return f"Code: {self.code}, Title: {self.title}, Author: {self.author}, Quantity: {self.quantity}"

class Inventory:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def update_quantity(self, code, quantity):
        for book in self.books:
            if book.code == code:
                book.quantity = quantity
                return True
        return False

    def search_book(self, code):
        for book in self.books:
            if book.code == code:
                return book
        return None

    def display_inventory(self):
        if not self.books:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            for book in self.books:
                print(book)

def main():
    inventory = Inventory()
    while True:
        print("\nWelcome to the Bookstore Inventory Management System")
        print("1. Add a new book")
        print("2. Update quantity of a book")
        print("3. Search for a book")
        print("4. Display inventory")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            code = input("Enter book code: ")
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            quantity = int(input("Enter quantity: "))
            book = Book(code, title, author, quantity)
            inventory.add_book(book)
            print("Book added to inventory.")

        elif choice == '2':
            code = input("Enter book code to update quantity: ")
            quantity = int(input("Enter new quantity: "))
            if inventory.update_quantity(code, quantity):
                print("Quantity updated successfully.")
            else:
                print("Book not found in inventory.")

        elif choice == '3':
            code = input("Enter book code to search: ")
            found_book = inventory.search_book(code)
            if found_book:
                print("Book found:")
                print(found_book)
            else:
                print("Book not found in inventory.")

        elif choice == '4':
            inventory.display_inventory()

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
