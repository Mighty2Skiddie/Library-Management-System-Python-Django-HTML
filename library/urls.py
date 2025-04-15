from django.urls import path
from .views import ( home,
    AuthorCreateView, BookCreateView, BorrowRecordCreateView,
    AuthorListView, BookListView, BorrowRecordListView, ExportToExcelView
)

urlpatterns = [
    path('', home, name='home'),
    path('add-author/', AuthorCreateView.as_view(), name='add-author'),
    path('add-book/', BookCreateView.as_view(), name='add-book'),
    path('add-borrow/', BorrowRecordCreateView.as_view(), name='add-borrow'),

    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('borrows/', BorrowRecordListView.as_view(), name='borrow-list'),
    path('export/', ExportToExcelView.as_view(), name='export-excel'),
    
]
