from django.shortcuts import render
from .forms import BookSearchForm
from .models import BookData

def index(request):
    form = BookSearchForm()
    books = BookData.objects.all()
    return render(request, 'books/index.html', locals())
