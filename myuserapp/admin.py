from django.contrib import admin

# Register your models here.

from . models import Student 
from .models import Category, Product


admin.site.register(Student)

admin.site.register(Category)
admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('title',)

admin.site.site_header = "Hetvi Project"
admin.site.site_title = "Hetvi Project Portal"
admin.site.index_title = "Welcome to Hetvi Project Dashboard"