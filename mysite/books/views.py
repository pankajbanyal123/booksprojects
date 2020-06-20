from django.shortcuts import render

from django.http import HttpResponse
from .models import Book
from django.template import loader

def index(request):
    all_books = Book.objects.all()
    template = loader.get_template('books/index.html')
    context= {
        'all_books':all_books
    }
    #html = ''
    #for book in all_books:
       # url = '/books/' + str(book.id) + '/'
       # html+= '<a href="' + url + '">' + str(book.name) + '</a><br>'



    return HttpResponse(template.render(context,request))
def detail(request, book_id):
    return HttpResponse("<h2> Details for Book Id:" + str(book_id) + "</h2>")
