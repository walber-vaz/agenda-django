from django.contrib import admin

from contacts.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'phone',
        'email',
        'created_date',
    )
    list_filter = ('created_date', 'last_name')
    search_fields = ('first_name', 'last_name', 'phone', 'email')
    ordering = ('last_name', 'first_name', 'created_date')
    date_hierarchy = 'created_date'
    fields = ('first_name', 'last_name', 'phone', 'email', 'description')
    readonly_fields = ('created_date',)
