
from django.contrib import admin
from django.urls import path,include
from library import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('library/', include('library.urls')),
    path('', include('library.urls')),
    
    
]
