import json
import os

FILE_NAME = "books.json"


def load_books():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_books(books):
    with open(FILE_NAME, "w") as file:
        json.dump(books, file, indent=4)


def add_book():
    books = load_books()

    book_id = input("Enter Book ID: ").strip()

    if not book_id or any(b["id"] == book_id for b in books):
        print("Invalid or duplicate Book ID!")
        return

    title = input("Enter Book Title: ").strip()
    author = input("Enter Author Name: ").strip()

    if not title or not author:
        print("Title and author cannot be empty!")
        return

    books.append({
        "id": book_id,
        "title": title,
        "author": author,
        "available": True,
        "issued_to": ""
    })

    save_books(books)
    print("Book added successfully!")


def display_books():
    books = load_books()

    if not books:
        print("No books found!")
        return

    for book in books:
        status = "Available" if book["available"] else "Issued"

        print("\nBook ID:", book["id"])
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Status:", status)


def search_book():
    books = load_books()
    book_id = input("Enter Book ID: ").strip()

    for book in books:
        if book["id"] == book_id:
            print("Book Found!")
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Available:", book["available"])
            return

    print("Book not found!")


def update_book():
    books = load_books()
    book_id = input("Enter Book ID to update: ").strip()

    for book in books:
        if book["id"] == book_id:
            title = input("Enter new title: ").strip()
            author = input("Enter new author: ").strip()

            if title:
                book["title"] = title

            if author:
                book["author"] = author

            save_books(books)
            print("Book updated successfully!")
            return

    print("Book not found!")


def delete_book():
    books = load_books()
    book_id = input("Enter Book ID to delete: ").strip()

    for book in books:
        if book["id"] == book_id:
            if not book["available"]:
                print("Cannot delete an issued book!")
                return

            books.remove(book)
            save_books(books)
            print("Book deleted successfully!")
            return

    print("Book not found!")


def issue_book():
    books = load_books()
    book_id = input("Enter Book ID to issue: ").strip()

    for book in books:
        if book["id"] == book_id:
            if not book["available"]:
                print("Book is already issued!")
                return

            student = input("Enter student name: ").strip()

            if not student:
                print("Student name cannot be empty!")
                return

            book["available"] = False
            book["issued_to"] = student

            save_books(books)
            print("Book issued successfully!")
            return

    print("Book not found!")


def return_book():
    books = load_books()
    book_id = input("Enter Book ID to return: ").strip()

    for book in books:
        if book["id"] == book_id:
            if book["available"]:
                print("Book is already available!")
                return

            book["available"] = True
            book["issued_to"] = ""

            save_books(books)
            print("Book returned successfully!")
            return

    print("Book not found!")


def main():
    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Issue Book")
        print("7. Return Book")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            display_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            update_book()
        elif choice == "5":
            delete_book()
        elif choice == "6":
            issue_book()
        elif choice == "7":
            return_book()
        elif choice == "8":
            print("Thank you!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()

