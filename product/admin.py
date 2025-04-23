from django.contrib import admin
from .models import Author, Genre, Post


admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Post)


























# from .models import Product


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'get_price_display', 'created_at')
#     search_fields = ('name',)
    
    
#     def get_price_display(self, obj):
#         return f"{obj.price} {obj.currency}"
 
#     get_price_display.short_description = 'Narx'
    
    

    
    

