"""
URL configuration for workshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import accounts.views as accounts
import books.views as books

urlpatterns = [
    path('admin/', admin.site.urls),
    # 登入
    path('login/', accounts.sign_in, name='Login'),
    # 登出
    path('logout/',accounts.log_out, name='Logout'),
    # 註冊
    path('register/', accounts.register, name='Register'),
    # 書籍管理
    path('', books.index, name='Book'),
    path('book/', books.index, name='Book'),
    # 書籍借閱記錄
    path('book_lend_records/<int:book_id>/', books.book_lend_record, name='BookLendRecord'),
    # 書籍詳細資訊
    path('book/<str:mode>/<int:book_id>', books.book_detail, name='BookDetail'),
    path('book/<str:mode>/', books.book_detail, name='BookDetail'),
    # 刪除書籍
    path('delete_book/', books.delete_book, name='DeleteBook'),
]