# 📚 Advanced Library Management System (Python)

This project is a **console-based Library Management System** developed using Python.
It is an improved and extended version of a basic library program, designed to demonstrate **clean code structure, logical problem-solving, and user input handling**.

The system allows users to manage a small library by adding books, checking them out, returning them, searching, and listing all available books through an interactive menu.

---

## 🎯 Purpose of the Project

This project was built to:

* Practice **real-world Python programming**
* Apply **control flow, loops, and functions**
* Handle **invalid user input safely**
* Prevent common logical errors in programs
* Build a **complete beginner-friendly project** suitable for a GitHub portfolio

---

## 🛠️ Technologies Used

* **Python 3**
* Built-in **os module** (for terminal screen management)

---

## 📦 Features

* ➕ Add new books with ISBN, title, and author
* 🚫 Prevent duplicate ISBN entries
* 📤 Check out books safely
* 📥 Check in returned books
* 📋 Display the full library catalog
* 🔍 Search books by title or author
* ⚠️ Handle invalid menu input gracefully
* 🧹 Clear terminal screen for better readability
* 🔁 Perform multiple operations without restarting the program

---

## 🧱 Data Structure

Books are stored in a dictionary using ISBN as a unique key:

```python
books = {
    "12345": {
        "title": "Python Basics",
        "author": "John Doe",
        "available": True
    }
}
```

### Why this structure?

* Fast access using ISBN
* Clear and readable data organization
* Easy to extend in the future (files, database, users, etc.)

---

## 🧠 Problems Solved & Design Decisions

### 1️⃣ Invalid Menu Input

* Uses `try / except` to prevent crashes when non-numeric input is entered.
* Ensures the program continues running safely.

### 2️⃣ Duplicate ISBNs

* Checks if an ISBN already exists before adding a new book.
* Prevents overwriting existing data.

### 3️⃣ Non-Existing Books

* Verifies ISBN existence before check-in or check-out.
* Displays clear error messages to the user.

### 4️⃣ Double Check-Out Prevention

* Prevents checking out a book that is already unavailable.

### 5️⃣ Double Check-In Prevention

* Prevents returning a book that is already available.

### 6️⃣ Continuous User Interaction

* Each operation runs in a loop, allowing repeated actions without restarting the program.

### 7️⃣ Cross-Platform Compatibility

* Uses `cls` for Windows and `clear` for Linux/macOS automatically.

---

## ▶️ How to Run the Program

1. Make sure **Python 3** is installed.
2. Save the code in a file, for example:

   ```bash
   library.py
   ```
3. Run the program:

   ```bash
   python library.py
   ```

---

## 📖 Menu Options

```
1. Add book
2. Check out a book
3. Check in a book
4. List books
5. Search books
6. Exit
```

---

## 🔍 Search Functionality

* Search by **book title**
* Search by **author name**
* Search is **case-insensitive**
* Displays all matching results

---

## 📌 Current Limitations

* Data is stored **in memory only**
* No file or database persistence
* No user authentication
* ISBN format is not validated

---

## 🔮 Future Improvements

* 💾 Save and load data using JSON
* 🧱 Convert the program to Object-Oriented Programming (OOP)
* 🖥️ Add a graphical user interface (Tkinter)
* 👤 Add user accounts and borrowing history
* 🧪 Add automated tests
