from django.contrib import admin
from .models import Book, BookInstance, Author, Genre

# Register your models here.

class BookInline(admin.TabularInline):
    model = Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'date_of_birth']
    fields = ['last_name', 'first_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]

class BooksInstanceInline(admin.StackedInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'display_genre']
    inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):

    list_display = ['id', 'book', 'status']
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'id','imprint')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )




#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)
