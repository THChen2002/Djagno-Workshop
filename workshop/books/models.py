from django.db import models
from accounts.models import Student

class BookCategory(models.Model):
    # 類別代號
    category_id = models.CharField(max_length=10)
    # 類別名稱
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name
    
class BookCode(models.Model):
    # 類別代號
    code_id = models.CharField(max_length=1)
    # 類別名稱
    code_name = models.CharField(max_length=100)

    def __str__(self):
        return self.code_name
    
class BookData(models.Model):
    # 書名
    name = models.CharField(max_length=100)
    # 類別
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)
    # 作者
    author = models.CharField(max_length=100, null=True)
    # 出版社
    publisher = models.CharField(max_length=100, null=True)
    # 出版日期
    publish_date = models.DateField(null=True)
    # 簡介
    summary = models.TextField(null=True)
    # 購買價格
    price = models.IntegerField(null=True)
    # 書籍保管人
    # keeper = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    keeper_id = models.IntegerField(null=True)
    # 書籍狀態
    status = models.ForeignKey(BookCode, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class BookLendRecord(models.Model):
    # 書籍
    book = models.ForeignKey(BookData, on_delete=models.CASCADE)
    # 借閱人
    borrower = models.ForeignKey(Student, on_delete=models.CASCADE)
    # 借閱日期
    borrow_date = models.DateField()

    def __str__(self):
        return self.book.name