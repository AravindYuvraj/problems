# A Simple Library Management System

print("Hello")


inventory = {
    "book1": {"title": "1984", "author": "George Orwell",  "year": 1949},
    "book2": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    "book3": {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
}

def display_books():
    print("Available books:")
    for book_id, book_info in inventory.items():
        print(f"{book_id}: {book_info['title']} by {book_info['author']} ({book_info['year']})")

def add_book(book_id, title, author, year):
    if book_id in inventory:
        print(f"Book ID {book_id} already exists.")
    else:
        inventory[book_id] = {"title": title, "author": author, "year": year}
        print(f"Book '{title}' added with ID {book_id}.")

def remove_book(book_id):
    if book_id in inventory:
        del inventory[book_id]
        print(f"Book ID {book_id} removed.")
    else:
        print(f"Book ID {book_id} not found.")

def main():
    while True:
        print("\nLibrary Management System")
        print("1. Display Books")
        print("2. Add Book")
        print("3. Remove Book")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_books()
        elif choice == '2':
            book_id = input("Enter book ID: ")
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = int(input("Enter publication year: "))
            add_book(book_id, title, author, year)
        elif choice == '3':
            book_id = input("Enter book ID to remove: ")
            remove_book(book_id)
        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 

