from django.shortcuts import render, redirect
from .models import book,author

# Books functions
def books(request):
    context = {
        "all_the_books" : book.objects.all()
    }
    return render(request, "books.html",context)


def add_book(request):
    book.objects.create(title = request.POST["book_title"], desc = request.POST["book_desc"])
    return redirect("/")


def view_book(request,book_id):
    thisBook = book.objects.get(id=int(book_id))
    assoc_authors = thisBook.authors.all()
    non_assoc_authors = author.objects.exclude(books=thisBook)
    context = {
        "thisBook" : thisBook,
        "assoc_authors" : assoc_authors,
        "non_assoc_authors" : non_assoc_authors
    }
    return render(request,"view_book.html",context)


def add_author_to_book(request,book_id):
    if request.POST['author_id']:
        thisBook = book.objects.get(id=int(book_id))
        thisAuthor = author.objects.get(id = request.POST['author_id'])
        thisBook.authors.add(thisAuthor)
    print(book_id)
    return redirect("/view_book/"+str(book_id))    


def go_to_books(request):
    return redirect("/")


# Authors functions

def authors(request):
    context = {
        "all_the_authors" : author.objects.all()
    }
    return render(request, "authors.html", context)


def add_author(request):
    author.objects.create(first_name = request.POST["first_name"], last_name = request.POST["last_name"], notes = request.POST["notes"])
    return redirect("/authors")


def view_author(request, author_id):
    thisAuthor = author.objects.get(id=int(author_id))
    assoc_books = thisAuthor.books.all()
    non_assoc_books = book.objects.exclude(authors = thisAuthor)
    context = {
        "thisAuthor" : thisAuthor,
        "assoc_books" : assoc_books,
        "non_assoc_books" : non_assoc_books
    }
    return render(request, "view_author.html",context)


def add_book_to_author(request, author_id):
    if request.POST['book_id']:
        thisAuthor = author.objects.get(id=int(author_id))
        thisBook = book.objects.get(id = request.POST['book_id'])
        thisAuthor.books.add(thisBook)
    return redirect("/view_author/"+ str(author_id))


def go_to_authors(request):
    return redirect("/authors")
