from django.shortcuts import render, redirect
import requests
import json
from .models import Book
from rest_framework import viewsets
from .serializers import BookSerializers
# Create your views here.
import django_filters.rest_framework
from rest_framework import generics
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse
from django.template import loader, Context

class BookView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'language', 'authors', 'date']
        
        
def books_list(request):
    new_books = []
    books = Book.objects.all()

    sort_by = request.POST.get("sort")  
    if sort_by:
        books = Book.objects.order_by('title')[:3000]
    else:
        pass

  
    def for_loop(url="https://www.googleapis.com/books/v1/volumes?q=Hobbit"):

        if request.method == 'POST':
            import_books = request.POST.get("import_books")   
            str(import_books)
        try:
            base_url = "https://www.googleapis.com/books/v1/volumes?q="
            url = base_url + import_books
        except:
            pass
        
        new_books = []
        json_data = requests.get(url).json()
        books_amount = len(books)

        if books_amount < 10:
            books_amount = 10
        else:
            pass

        for book_num in range(0, books_amount):
            try:
                title = json_data['items'][book_num]['volumeInfo']['title']
                existing_books = []

                for exist in books:
                    x = exist.title
                    existing_books.append(x)

                if title in existing_books:
                    pass
                
                else:
                    authors_raw = json_data['items'][book_num]['volumeInfo']['authors']
                    date = json_data['items'][book_num]['volumeInfo']['publishedDate']

                    for aut in authors_raw:
                        authors = ""
                        authors += aut
                        authors += " "
                    if len(date) == 4:
                        date += "-01-01"
                    elif len(date) == 7:
                        date += "-01"

                    else:
                        date = json_data['items'][book_num]['volumeInfo']['publishedDate']
                    try:
                        pages = json_data['items'][book_num]['volumeInfo']['pageCount']
                    except:
                        pages = 0

                    language = json_data['items'][book_num]['volumeInfo']['language']
                    try:
                        link = json_data['items'][book_num]['volumeInfo']['imageLinks']['thumbnail']
                    except:
                        link = ""

                    new_book = Book()
                    new_book.title = title 
                    new_book.authors = authors
                    new_book.link = link
                    new_book.language = language


                    new_book.pages = pages
                    new_book.date = date
                    new_book.save()
            except:
                book_num -= 1
    for_loop()

    search_title = request.POST.get("title")  
    search_authors = request.POST.get("authors")   
    str(search_title)
    str(search_authors)
 
    try:
        if search_title != "":
            for book in books:
                if search_title.lower() in book.title.lower():
                    new_books.append(book)
                else:
                    pass
        elif search_authors != "":
            for book in books:
                if search_authors in book.authors:
                    new_books.append(book)
                else:
                    pass
    except:
        pass
    search_authors = request.POST.get("authors")   
    str(search_authors)

    try:
        if search_authors != "":
            for book in books:
                if search_authors.lower() in book.authors.lower():
                    new_books.append(book)
                else:
                    pass
    except:
        pass
    search_language = request.POST.get("language")   
    str(search_language)

    try:
        if search_language != "":
            for book in books:
                if search_language.lower() in book.language:
                    new_books.append(book)
                else:
                    pass
    except:
        pass

    try:
        search_date = request.POST.get("date")
        str(search_date)

        searched_split_date = search_date.split(",")
        searched_split_date_1 = searched_split_date[0].split("-")
        searched_split_date_2 = searched_split_date[1].split("-")
        
        if len(searched_split_date_1) <= 4 and len(searched_split_date_2) <= 4:
            year_1 = searched_split_date_1[0]
            month_1 = "01"
            day_1 = "01"
            year_2 = searched_split_date_2[0]
            month_2 = "01"
            day_2 = "01"    
        else:
            year_1 = searched_split_date_1[0]
            month_1 = searched_split_date_1[1]
            day_1 = searched_split_date_1[2]
            year_2 = searched_split_date_2[0]
            month_2 = searched_split_date_2[1]
            day_2 = searched_split_date_2[2]

        for book in books:
            string_date = str(book.date)
            book_date = string_date.split("-")
            book_year = int(book_date[0])
            book_month = book_date[1]
            book_day = book_date[2]

            date_1 = int(str(year_1) + str(month_1) + str(day_1))
            date_2 = int(str(year_2) + str(month_2) + str(day_2))

            book_date_int = int(str(book_year) + str(book_month) + str(book_day))

            if date_1 <= book_date_int <= date_2:
                new_books.append(book)
            else:
                pass
    except:
        pass

    import_books = request.POST.get("import_books")   
    str(import_books)
    try:
        base_url = "https://www.googleapis.com/books/v1/volumes?q="
        new_url = base_url + import_books
        for_loop(new_url)
    except:
        pass
    context = {
        'books': books,
        'new_books': new_books,    
    }

    return render(request, "books.html", context)


def add_book(request):
    new_book = Book()
    if request.method == 'POST':
        new_book = Book()
        try:
            new_book.title = request.POST.get('title')
            new_book.authors = request.POST.get('authors')
            new_book.pages = request.POST.get('pages')
            new_book.link = request.POST.get('link')
            new_book.date = request.POST.get('date')
            new_book.language = request.POST.get('language')
            new_book.save()
        except:
            pass
    
    context = {
        'new_boook': new_book,
    }
    return render(request, "add_book.html", context)


def delete_books(request):
    books = Book.objects.all()
    books.delete()

    return redirect('/books/')
