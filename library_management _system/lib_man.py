import mysql.connector

class LibraryManager:
    def __init__(self, host, user, password, database):
        try:
            self.db = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            self.cursor = self.db.cursor()
            self.create_table()
            print("Connected to database successfully!")
        except mysql.connector.Error as err:
            print("Database connection error:", err)

    def create_table(self):
        try:
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255),
                author VARCHAR(255),
                isbn VARCHAR(255)
            )
            """)
            print("Books table is ready!")
        except mysql.connector.Error as err:
            print("Error creating table:", err)

    def add_book(self, title, author, isbn):
        try:
            sql = "INSERT INTO books (title, author, isbn) VALUES (%s, %s, %s)"
            self.cursor.execute(sql, (title, author, isbn))
            self.db.commit()
        except mysql.connector.Error as err:
            print("Error adding book:", err)
        else:
            print("Book added successfully.")

    def search_books_by_title(self, title):
        try:
            sql = "SELECT * FROM books WHERE title LIKE %s"
            self.cursor.execute(sql, ('%' + title + '%',))
            results = self.cursor.fetchall()
        except mysql.connector.Error as err:
            print("Error searching for books:", err)
        else:
            if results:
                print("Search Results:")
                for book in results:
                    print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, ISBN: {book[3]}")
            else:
                print("No matching books found.")

    def list_all_books(self):
        try:
            self.cursor.execute("SELECT * FROM books")
            books = self.cursor.fetchall()
        except mysql.connector.Error as err:
            print("Error retrieving books:", err)
        else:
            if books:
                print("All Books:")
                for book in books:
                    print(f"ID: {book[0]} | Title: {book[1]} | Author: {book[2]} | ISBN: {book[3]}")
            else:
                print("Library is empty.")

    def delete_book(self, book_id):
        try:
            sql = "DELETE FROM books WHERE id = %s"
            self.cursor.execute(sql, (book_id,))
            self.db.commit()
        except mysql.connector.Error as err:
            print("Error deleting book:", err)
        else:
            if self.cursor.rowcount:
                print("Book deleted successfully.")
            else:
                print("Book not found.")

    def close(self):
        try:
            self.cursor.close()
            self.db.close()
        except mysql.connector.Error as err:
            print("Error closing connection:", err)
        else:
            print("Database connection closed.")


# -------------------
# 🧪 Example Usage
# -------------------
if __name__ == "__main__":
    try:
        manager = LibraryManager(
            host="localhost",
            user="yourusername",
            password="yourpassword",
            database="library"
        )

        manager.add_book("Brave New World", "Aldous Huxley", "111122223333")
        manager.add_book("The Great Gatsby", "F. Scott Fitzgerald", "444455556666")

        manager.list_all_books()
        manager.search_books_by_title("gatsby")

        manager.delete_book(1)
        manager.list_all_books()

    except Exception as e:
        print("Unexpected error:", e)

    finally:
        if 'manager' in locals():
            manager.close()
