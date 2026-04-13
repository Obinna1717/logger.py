import sqlite3

# Connect to database (creates file if it doesn't exist)
conn = sqlite3.connect("books.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    year_published INTEGER
)
""")
conn.commit()


# وظائف (Functions)

def add_book():
    title = input("Enter title: ")
    author = input("Enter author: ")
    year = int(input("Enter year published: "))

    cursor.execute("INSERT INTO books (title, author, year_published) VALUES (?, ?, ?)",
                   (title, author, year))
    conn.commit()
    print("Book added successfully!")


def view_all_books():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    if books:
        for book in books:
            print(book)
    else:
        print("No books found.")


def search_books_by_author():
    author = input("Enter author name: ")

    cursor.execute("SELECT * FROM books WHERE author LIKE ?", ('%' + author + '%',))
    books = cursor.fetchall()

    if books:
        for book in books:
            print(book)
    else:
        print("No books found for that author.")


def update_book_year():
    book_id = int(input("Enter book ID: "))
    new_year = int(input("Enter new year: "))

    cursor.execute("UPDATE books SET year_published = ? WHERE id = ?", (new_year, book_id))
    conn.commit()
    print("Book updated successfully!")


def delete_book():
    book_id = int(input("Enter book ID to delete: "))

    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    print("Book deleted successfully!")


# CLI Menu

def menu():
    while True:
        print("\n--- Book Tracker ---")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search by Author")
        print("4. Update Book Year")
        print("5. Delete Book")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_all_books()
        elif choice == "3":
            search_books_by_author()
        elif choice == "4":
            update_book_year()
        elif choice == "5":
            delete_book()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


# Run program
menu()

# Close connection when done
conn.close()