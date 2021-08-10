from django.contrib import admin
from django.contrib.admin.decorators import action
from .models import Product

# Register your models here.
class productAdmin(admin.ModelAdmin):
    
    def change_category_to_default(self, request, queryset):
        queryset.update(category = 'default')
    
    # change_category_to_default.short_description = "default category"
    list_display = ('title', 'price', 'discount_price', 'category', 'description')
    search_fields = ('title',)
    list_editable = ('price', 'category')
    actions = ("change_category_to_default")

admin.site.site_header = "E-commerce site"
admin.site.site_title = "Abc shopping"
admin.site.index_title  = "manage your shope"
admin.site.register(Product, productAdmin)



