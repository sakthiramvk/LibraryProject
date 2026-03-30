# Simple Library Management System (Beginner Level)
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username == "admin" and password == "123":
        print("Login successful!\n")
    else:
        print("Invalid login!\n")

login()


library = []

def add_book():
    book = input("Enter book name: ")
    library.append(book)
    print("Book added successfully!\n")

def view_books():
    if len(library) == 0:
        print("No books in library\n")
    else:
        print("Books in library:")
        for i, book in enumerate(library, start=1):
            print(f"{i}. {book}")
        print()

def remove_book():
    book = input("Enter book name to remove: ")
    if book in library:
        library.remove(book)
        print("Book removed successfully!\n")
    else:
        print("Book not found!\n")

while True:
    print("==== Library Menu ====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Remove Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_book()
    elif choice == '2':
        view_books()
    elif choice == '3':
        remove_book()
    elif choice == '4':
        print("Exiting program...")
        break
    else:
        print("Invalid choice!\n")