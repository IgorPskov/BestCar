from django.contrib import admin

from cars.models import Categories, Products

# admin.site.register(Categories)
# admin.site.register(Products)

class ProductsTabAdmin(admin.TabularInline):
    model = Products
    fields = 'name', 'year', 'mileage', 'price'
    search_fiels =  'name', 'year', 'mileage', 'price'
    readonly_fields = ('name', 'year', 'mileage',)
    extra = 1

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'category', 'price', 'discount', 'year', 'mileage']
    list_editable = ['price', 'discount']
    search_fields = ['name', 'category__name']
    list_filter = ['category__name', 'price', 'year', 'mileage', 'discount']
    ordering = ['category__name'] 
    fields = [
        'category',
        'name',
        'slug',
        'year',
        'engine',
        'power',
        'mileage',
        'gearbox',
        'fuel',
        'color',
        'description',
        'image',
        'image2',
        'image3',
        ('price', 'discount'),
    ]


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']
    list_filter = ['name']

    inlines = [ProductsTabAdmin]