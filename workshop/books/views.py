from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q
from .forms import BookSearchForm, BookDataForm
from .models import BookData, BookLendRecord
from accounts.models import Student

def index(request):
    books = BookData.objects.all()
    if request.method == 'POST':
        form = BookSearchForm(request.POST)
        if form.is_valid():
            book_name = form.cleaned_data['book_name']
            category_id = form.cleaned_data['category']
            borrower_id = form.cleaned_data['borrower']
            book_status = form.cleaned_data['book_status']

            # 構建查詢條件
            conditions = Q()
            if book_name:
                conditions &= Q(name__contains=book_name)
            if category_id:
                conditions &= Q(category_id=category_id)
            if borrower_id:
                conditions &= Q(keeper_id=borrower_id)
            if book_status:
                conditions &= Q(status_id=book_status)

            books = books.filter(conditions)
    else:
        form = BookSearchForm()
    return render(request, 'books/index.html', locals())

def book_detail(request, book_id):
    book = BookData.objects.get(id=book_id)
    if request.method == 'POST':
        form = BookDataForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect(reverse('BookDetail', args=[book_id]))
    else:
        form = BookDataForm(instance=book)
    return render(request, 'books/book_detail.html', locals())

def book_lend_record(request, book_id):
    records = BookLendRecord.objects.filter(book_id=book_id).order_by('-borrow_date')
    return render(request, 'books/book_lend_record.html', locals())
