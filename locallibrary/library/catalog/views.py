from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Book, BookInstance, Author, Genre

# Create your views here.

def index(request):

    number_of_books = Book.objects.all().count()
    number_instances = BookInstance.objects.all().count()
    number_instances_available = BookInstance.objects.filter(status__exact = 'a').count()
    number_authors = Author.objects.count()
    comic_books = Book.objects.filter(genre__name__icontains = 'omic').count()

    context = {

        'total_books' : number_of_books,
        'all_instances' : number_instances,
        'available_instances' : number_instances_available,
        'total_authors' : number_authors,
        'comic_books' : comic_books
    }

    return render(request, 'index.html', context=context)


def register(request):

    if request.method =='POST':

        first_name = request.POST['fname']
        last_name = request.POST['lname']
        uname = request.POST['uname']
        password = request.POST['password']
        confirm_password = request.POST['password1']
        email_address = request.POST['email']

        if (password == confirm_password):

            if User.objects.filter(username=uname).exists():
                messages.info(request, 'User is Already Exists')
                return render(request, 'register.html', context= None)

            elif User.objects.filter(email=email_address).exists():
                messages.info(request, 'Email is Already Exists')
                return render(request, 'register.html', context= None)

            else:
                user = User.objects.create_user(username=uname, password=password, email=email_address, first_name=first_name, last_name=last_name)
                user.save()
                print('User created successfully...')
                return render(request, 'login.html', context= None)

        else:

            messages.info(request, 'Passwords not matching..')
            return render(request, 'register.html', context= None)

    else:

        return render(request, 'register.html', context= None)


def login(request):

    if request.method == 'POST':

        username = request.POST['uname']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            print('Invalid Credentials..')
            messages.info(request, 'Invalid Credentials..')
            return redirect('login')
    else:

        return render(request, 'login.html', context= None)

def logout(request):

    auth.logout(request)
    return redirect('login')


class BooksListView(generic.ListView):

    model=Book
    context_object_name = 'my_books'
    teemplate_name = 'book_list.html'

class BookDetailView(generic.DetailView):

    model = Book
    context_object_name = 'selected_book'
    template_name = 'book_detail.html'

class AuthorListView(generic.ListView):

    model=Author
    context_object_name = 'all_authors'
    template_name = 'author_list.html'

class AuthorDetailView(generic.DetailView):

    model = Author
    context_object_name = 'selected_author'
    template_name = 'author_detail.html'
