from django.contrib import admin

from contacts.models import Contact


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
    )
    list_filter = ('created_date',)
    search_fields = ('first_name', 'last_name', 'phone', 'email')
    ordering = ('-id', 'last_name', 'first_name', 'created_date')
    date_hierarchy = 'created_date'
    fields = (
        'first_name',
        'last_name',
        'phone',
        'email',
        'description',
        'show',
        'picture',
    )
    readonly_fields = ('created_date',)
    list_per_page = 10
    list_max_show_all = 100
    list_display_links = ('id', 'first_name')
