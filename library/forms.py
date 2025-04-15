from django import forms
from .models import Author, Book, BorrowRecord

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email', 'bio']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith("@gmail.com"):
            raise forms.ValidationError("Email must be a Gmail address.")
        return email

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'genre', 'published_date', 'author']

class BorrowRecordForm(forms.ModelForm):
    class Meta:
        model = BorrowRecord
        fields = ['user_name', 'book', 'borrow_date', 'return_date']
