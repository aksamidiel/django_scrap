from django.contrib import admin
from core import models


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name', 'urls']
    list_display = ['__unicode__', 'sort']
    list_editable = ('sort',)
    list_filter = ('root_category',)


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name', 'urls', 'description']
    list_display = ('__unicode__', 'price', 'sort')
    list_editable = ('sort',)
    list_filter = ('category',)


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Category, CategoryAdmin)

