import os
from datetime import datetime

class Book:
    def __init__(self, title, author, isbn, is_issued=False, added_on=None, issued_on=None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_issued = is_issued
        self.added_on = added_on or datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.issued_on = issued_on

    def __str__(self):
        status = 'Issued' if self.is_issued else 'Available'
        return (f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status} "
                f"(Added on: {self.added_on}){' - Issued on: ' + self.issued_on if self.is_issued else ''}")

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_issued:
            print(f"Book '{book.title}' is already issued to someone else.")
        else:
            book.is_issued = True
            book.issued_on = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.borrowed_books.append(book)
            print(f"Book '{book.title}' issued to {self.name} on {book.issued_on}.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_issued = False
            book.issued_on = None
            self.borrowed_books.remove(book)
            print(f"Book '{book.title}' returned by {self.name} on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.")
        else:
            print(f"{self.name} does not have this book.")

    def __str__(self):
        borrowed_books_titles = [book.title for book in self.borrowed_books]
        return f"User: {self.name} (ID: {self.user_id}) - Borrowed Books: {borrowed_books_titles}"

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.load_data()

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library on {book.added_on}.")

    def add_user(self, user):
        self.users.append(user)
        print(f"User '{user.name}' added to the library system.")

    def issue_book(self, user_id, isbn):
        user = self.find_user(user_id)
        book = self.find_book(isbn)
        if user and book:
            user.borrow_book(book)

    def return_book(self, user_id, isbn):
        user = self.find_user(user_id)
        book = self.find_book(isbn)
        if user and book:
            user.return_book(book)

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        print(f"No book found with ISBN: {isbn}")
        return None

    def find_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        print(f"No user found with ID: {user_id}")
        return None

    def list_books(self):
        for book in self.books:
            print(book)

    def list_users(self):
        for user in self.users:
            print(user)

    def save_data(self):
        with open('books.txt', 'w') as book_file:
            for book in self.books:
                book_file.write(f"{book.title},{book.author},{book.isbn},{book.is_issued},"
                                f"{book.added_on},{book.issued_on or ''}\n")

        with open('users.txt', 'w') as user_file:
            for user in self.users:
                borrowed_isbns = ','.join([book.isbn for book in user.borrowed_books])
                user_file.write(f"{user.name},{user.user_id},{borrowed_isbns}\n")

        with open('issued_books.txt', 'w') as issued_file:
            for user in self.users:
                for book in user.borrowed_books:
                    issued_file.write(f"{user.user_id},{book.isbn},{book.issued_on}\n")

    def load_data(self):
        if os.path.exists('books.txt'):
            with open('books.txt', 'r') as book_file:
                for line in book_file:
                    data = line.strip().split(',')
                    if len(data) == 6:  # Ensure the correct number of elements are present
                        title, author, isbn, is_issued, added_on, issued_on = data
                        book = Book(title, author, isbn, is_issued == 'True', added_on, issued_on or None)
                        self.books.append(book)
                    else:
                        print(f"Skipped invalid line in books.txt: {line}")

        if os.path.exists('users.txt'):
            with open('users.txt', 'r') as user_file:
                for line in user_file:
                    data = line.strip().split(',')
                    if len(data) >= 2:  # Basic validation
                        name, user_id, *borrowed_isbns = data
                        user = User(name, user_id)
                        self.users.append(user)
                        for isbn in borrowed_isbns:
                            book = self.find_book(isbn)
                            if book:
                                user.borrow_book(book)

        if os.path.exists('issued_books.txt'):
            with open('issued_books.txt', 'r') as issued_file:
                for line in issued_file:
                    data = line.strip().split(',')
                    if len(data) == 3:  # Ensure the correct number of elements are present
                        user_id, isbn, issued_on = data
                        user = self.find_user(user_id)
                        book = self.find_book(isbn)
                        if user and book:
                            book.issued_on = issued_on
                            user.borrow_book(book)

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Add User")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. List Books")
        print("6. List Users")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            book = Book(title, author, isbn)
            library.add_book(book)
        elif choice == '2':
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            user = User(name, user_id)
            library.add_user(user)
        elif choice == '3':
            user_id = input("Enter user ID: ")
            isbn = input("Enter book ISBN: ")
            library.issue_book(user_id, isbn)
        elif choice == '4':
            user_id = input("Enter user ID: ")
            isbn = input("Enter book ISBN: ")
            library.return_book(user_id, isbn)
        elif choice == '5':
            library.list_books()
        elif choice == '6':
            library.list_users()
        elif choice == '7':
            library.save_data()
            print("Exiting system. Data saved.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
