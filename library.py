import csv
import os

FILE_NAME = "books.csv"

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Book ID", "Title", "Author", "Status"])
        writer.writerow([book_id, title, author, "Available"])

    print("✅ Book added successfully\n")

def view_books():
    if not os.path.isfile(FILE_NAME):
        print("❌ No books found\n")
        return

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    print()

def issue_book():
    book_id = input("Enter Book ID to issue: ")
    rows = []

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    for row in rows[1:]:
        if row[0] == book_id and row[3] == "Available":
            row[3] = "Issued"
            print("✅ Book issued\n")
            break
    else:
        print("❌ Book not available\n")

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

def return_book():
    book_id = input("Enter Book ID to return: ")
    rows = []

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    for row in rows[1:]:
        if row[0] == book_id and row[3] == "Issued":
            row[3] = "Available"
            print("✅ Book returned\n")
            break
    else:
        print("❌ Invalid Book ID\n")

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

def main():
    while True:
        print("===== Library Management System =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            issue_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            print("👋 Exiting program")
            break
        else:
            print("❌ Invalid choice\n")

main()
