from django.contrib import admin
from django.urls import path
from catalog import views

urlpatterns = [

    path('', views.index, name='index'),
    path('books/', views.BooksListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('register/', views.register, name='register'),
    path('register/validate_user', views.register, name='validate_user'),
    path('login/', views.login, name='login'),
    path('login/validate_login', views.login, name='validate_login'),
    path('logout/', views.logout, name='logout'),

]
