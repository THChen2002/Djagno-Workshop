from django.contrib import admin
from books.models import BookCategory, BookCode, BookData, BookLendRecord

class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category_id", "category_name")
    ordering = ("id",)

class BookCodeAdmin(admin.ModelAdmin):
    list_display = ("id", "code_id", "code_name")
    ordering = ("id",)

class BookDataAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "author", "publisher", "publish_date", "price", "keeper_id", "status")
    list_filter = ("category", "status")
    search_fields=('name',)
    ordering = ("id",)

class BookLendRecordAdmin(admin.ModelAdmin):
    list_display = ("id", "book", "borrower", "borrow_date")
    search_fields=('book__name',)
    ordering = ("-borrow_date",)

admin.site.register(BookCategory, BookCategoryAdmin)
admin.site.register(BookCode, BookCodeAdmin)
admin.site.register(BookData, BookDataAdmin)
admin.site.register(BookLendRecord, BookLendRecordAdmin)
