from django.shortcuts import render, redirect
from django.views import View

from .forms import AddBookForm
from .models import AddBookModel

# Create your views here.
# Function for landing page after clicking on books button present on dashboard
class Home(View):
    def get(self, request):
        books = AddBookModel.objects.all()
        context = {'books': books}
        return render(request, 'books/home.html', context)

# Function for adding new books
def add(request):
    # Accessing the form to add details of a book
    form=AddBookForm()
    if request.method=='POST':
        form=AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form=AddBookForm()
    context={'form': form}
    return render(request, 'books/add.html', context)

# Function for editing an existing book
def edit(request, pk):
    # Get the details of that particular book
    books=AddBookModel.objects.get(id=pk)
    form=AddBookForm(instance=books)
    if request.method=='PUT':
        form=AddBookForm(request.POST, instance=books)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form': form}
    return render(request, 'books/edit.html', context)

# Function to delete a particular book details 
def delete(request, pk):
    # Get the details of that particular book
    books=AddBookModel.objects.get(id=pk)
    if request.method=='DELETE':
        books.delete()
        return redirect('home')
    context={'book': books}
    return render(request, 'books/delete.html', context)