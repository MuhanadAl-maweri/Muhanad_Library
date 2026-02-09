import os

books = {}

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def menu():
    print("\nLibrary Menu:")
    print("1. Add book")
    print("2. Check out a book")
    print("3. Check in a book")
    print("4. List books")
    print("5. Search books")
    print("6. Exit")


def add_book():
    while True:
        clear_screen()
        isbn = input("Enter ISBN: ").strip()

        if isbn in books:
            print("❌ This ISBN already exists.")
        else:
            title = input("Enter title: ").strip().title()
            author = input("Enter author: ").strip().title()
            books[isbn] = {
                "title": title,
                "author": author,
                "available": True
            }
            print(f"✅ Book '{title}' added successfully.")

        if input("Add another book? (y/n): ").lower() == "n":
            break


def check_out():
    while True:
        clear_screen()
        isbn = input("Enter ISBN to check out: ").strip()

        if isbn not in books:
            print("❌ Book not found.")
        elif not books[isbn]["available"]:
            print("❌ Book is already checked out.")
        else:
            books[isbn]["available"] = False
            print(f"✅ Book '{books[isbn]['title']}' checked out.")

        if input("Check out another book? (y/n): ").lower() == "n":
            break


def check_in():
    while True:
        clear_screen()
        isbn = input("Enter ISBN to check in: ").strip()

        if isbn not in books:
            print("❌ Book not found.")
        elif books[isbn]["available"]:
            print("❌ Book is already checked in.")
        else:
            books[isbn]["available"] = True
            print(f"✅ Book '{books[isbn]['title']}' checked in.")

        if input("Check in another book? (y/n): ").lower() == "n":
            break


def list_books():
    clear_screen()
    if not books:
        print("Library is empty.")
    else:
        print("📚 Library Catalog:\n")
        for isbn, data in books.items():
            print(
                f"ISBN: {isbn} | "
                f"Title: {data['title']} | "
                f"Author: {data['author']} | "
                f"Available: {data['available']}"
            )
    input("\nPress Enter to return to menu...")


def search_books():
    clear_screen()
    keyword = input("Enter title or author to search: ").lower()
    found = False

    for isbn, data in books.items():
        if keyword in data["title"].lower() or keyword in data["author"].lower():
            print(
                f"ISBN: {isbn} | "
                f"Title: {data['title']} | "
                f"Author: {data['author']} | "
                f"Available: {data['available']}"
            )
            found = True

    if not found:
        print("❌ No matching books found.")

    input("\nPress Enter to return to menu...")


# Main loop
while True:
    clear_screen()
    menu()

    try:
        choice = int(input("Choose an option (1-6): "))
    except ValueError:
        print("❌ Invalid input. Please enter a number.")
        input("Press Enter to continue...")
        continue

    if choice == 1:
        add_book()
    elif choice == 2:
        check_out()
    elif choice == 3:
        check_in()
    elif choice == 4:
        list_books()
    elif choice == 5:
        search_books()
    elif choice == 6:
        print("👋 Exiting program...")
        break
    else:
        print("❌ Invalid choice. Choose between 1 and 6.")
        input("Press Enter to continue...")
