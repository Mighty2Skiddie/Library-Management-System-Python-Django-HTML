# Library-Management-System-Python-Django-HTML
A Django web application that allows administrators to manage authors, books, and borrow records in a simple, elegant library system. Built using Python, Django, HTML, and styled with inline CSS for immediate visual appeal.

# Features

- Add, list, and manage Authors

- Add, list, and manage Books, with author assignment

- Track Borrow Records (user who borrowed, book, and return date)

- Paginated views for better readability

- Export data to Excel: authors, books, and borrow records on separate sheets

# Project Structure

![Screenshot 2025-04-15 200343](https://github.com/user-attachments/assets/1c8e1061-72d3-449c-8db2-9d142c4f9737)


# Setup Instructions
1. Prerequisites

Make sure Python 3.10+ and Django 4.2+ are installed.  

pip install django openpyxl

2. Create Project

django-admin startproject library_system
cd library_system
python manage.py startapp library

3. Add to INSTALLED_APPS in settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'library',  # <-- add this
]

# Models Summary

Author

name: CharField

email: EmailField (unique)

bio: TextField

Book

title: CharField

genre: CharField

published_date: DateField

author: ForeignKey to Author

BorrowRecord

user_name: CharField

book: ForeignKey to Book

borrow_date: DateField

return_date: DateField

# Forms

AuthorForm

Validates email

Uses forms.ModelForm

BookForm

Dropdown for authors

Date input for published_date

BorrowRecordForm

Standard model form

# Views & URLs

Uses class-based views (CBVs) for clarity.

/ → Home page

/add-author/ → Create new author

/add-book/ → Create new book

/add-borrow/ → Create new borrow record

/authors/ → List of authors (paginated)

/books/ → List of books (paginated)

/borrows/ → List of borrow records (paginated)

/export/ → Download all data as Excel file

# Export to Excel

Implemented using openpyxl. Exported sheets:

Authors: ID, Name, Email, Bio

Books: ID, Title, Genre, Published Date, Author

Borrow Records: ID, User, Book, Borrow Date, Return Date

Visit /export/ to download all at once.

# Running the Project

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

Go to http://127.0.0.1:8000/ in your browser.

# Contributions

Feel free to fork, improve, and submit a pull request.

# License

MIT License

# Screenshot
![Screenshot 2025-04-15 200908](https://github.com/user-attachments/assets/8919b8ee-79dc-443f-a0d2-b8ed6809b974)

![Screenshot 2025-04-15 201039](https://github.com/user-attachments/assets/ed95c1c1-3586-4d9c-8380-341e13731136)

![Screenshot 2025-04-15 201141](https://github.com/user-attachments/assets/60d452a9-84e0-4f1f-98af-feef4c4070c9)

![Screenshot 2025-04-15 201236](https://github.com/user-attachments/assets/92002064-1fe7-4126-9ed5-9fca23528291)

![Screenshot 2025-04-15 201548](https://github.com/user-attachments/assets/7695112c-fcb8-446d-b20d-918ab314f5c6)








Made with ❤️ using Django.



