from django import forms
from .models import BookCategory, BookCode, BookData
from accounts.models import Student
from datetime import datetime

class BookSearchForm(forms.Form):
    book_name = forms.CharField(
        label='書名',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'BookName'})
    )
    category_choices = [('', '----------------- 圖書類別 -----------------')] + list(BookCategory.objects.values_list('id', 'category_name'))
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
    book_status_choices = [('', '----------------- 借閱狀態 -----------------')] + list(BookCode.objects.values_list('id', 'code_name'))
    book_status = forms.ChoiceField(
        label='狀態',
        choices=book_status_choices,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'BookStatus'})
    )

class BookDataForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookDataForm, self).__init__(*args, **kwargs)
        self.fields['author'].required = False
        self.fields['publisher'].required = False
        self.fields['publish_date'].required = False
        self.fields['summary'].required = False
        self.fields['price'].required = False
        self.fields['keeper_id'].required = False

    keeper = forms.ChoiceField(
        label='借閱人',
        choices=[('', '------------------ 借閱人 ------------------')] + list(Student.objects.values_list('id', 'username')),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    class Meta:
        model = BookData
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'},),
            'publisher': forms.TextInput(attrs={'class': 'form-control'}),
            'publish_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date' ,'max': datetime.now().strftime('%Y-%m-%d')}),
            'summary': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'keeper_id': forms.HiddenInput(),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': '書名',
            'category': '圖書類別',
            'author': '作者',
            'publisher': '出版社',
            'publish_date': '出版日期',
            'summary': '內容簡介',
            'price': '價格',
            'keeper_id': '借閱人',
            'status': '借閱狀態',
        }

