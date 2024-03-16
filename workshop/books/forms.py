from django import forms
from .models import BookCategory
from accounts.models import Student

class BookSearchForm(forms.Form):
    book_name = forms.CharField(
        label='書名',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'BookName'})
    )
    category_choices = [('', '----------------- 圖書類別 -----------------')] + list(BookCategory.objects.values_list('category_id', 'category_name'))
    category = forms.ChoiceField(
        label='圖書類別',
        choices=category_choices,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'Category'})
    )
    borrower_choices = [('', '------------------ 借閱人 ------------------')] + list(Student.objects.values_list('id', 'username'))
    borrower = forms.ChoiceField(
        label='借閱人',
        choices=borrower_choices,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'Borrower'})
    )
    book_status_choices = [('', '------------------- 狀態 -------------------'), ('Y', '可借閱'), ('N', '不可借出'), ('B', '已借閱')]
    book_status = forms.ChoiceField(
        label='狀態',
        choices=book_status_choices,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'BookStatus'})
    )

