from django.shortcuts import render,redirect
from .models import Book,Author

def add_book(request):
    if request.method =='POST':
        Book.objects.create(
            title= request.POST['title'],
            desc= request.POST['desc']
        )
        return redirect('/books')
    books= Book.objects.all()
    return render(request,'add_book.html', {'books':books})
        
def add_author(request):
    if request.method =='POST':
        Author.objects.create(
            first_name= request.POST['first_name'],
            last_name= request.POST['last_name'],
            notes= request.POST['notes']
        )
        return redirect('/authors')
    authors= Author.objects.all()
    return render(request, 'add_author.html', {'authors':authors})

def book_detail(request,id):
    book= Book.objects.get(id=id)
    if request.method == 'POST':
        author_id = request.POST['author_id']
        author = Author.objects.get(id=author_id)
        book.authors.add(author)
        return redirect('book_detail', id=id)
    #focus I return all authors for options in html :) in the html i call book.authors.all to get the authors for the book
    return render(request,'book_detail.html',{'book':book, 'authors':Author.objects.all()})

def author_detail(request, id):
    author = Author.objects.get(id=id)
    if request.method == 'POST':
        book_id = request.POST['book_id']
        book = Book.objects.get(id=book_id)
        author.books.add(book)
        return redirect('author_detail', id=id)

    context = {
        'author': author,
        'books': Book.objects.all()
    }
    return render(request,'author_detail.html',context)
    
