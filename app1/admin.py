from django.contrib import admin
from .models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['Book_id','Book_name','Book_author','Book_publish_year','Book_price']
admin.site.register(Book,BookAdmin)    