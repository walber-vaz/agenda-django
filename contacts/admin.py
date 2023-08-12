from django.contrib import admin

from contacts.models import Category, Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'phone',
        'email',
        'created_date',
        'show',
        'picture',
        'category',
    )
    list_filter = ('created_date', 'show', 'category')
    search_fields = ('first_name', 'last_name', 'phone', 'email', 'category')
    ordering = ('-id', 'last_name', 'first_name', 'created_date', 'category')
    date_hierarchy = 'created_date'
    fields = (
        'first_name',
        'last_name',
        'phone',
        'email',
        'description',
        'category',
        'show',
        'picture',
    )
    readonly_fields = ('created_date',)
    list_per_page = 10
    list_max_show_all = 100
    list_display_links = ('id', 'first_name')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('-id', 'name')
    fields = ('name',)
    list_per_page = 10
    list_max_show_all = 100
    list_display_links = ('id', 'name')
