from django.urls import path

from contacts import views

app_name = "contacts"

urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    # contact
    path("contact/<int:contact_id>/detail/", views.contact, name="contact"),
    path("contact/create/", views.create, name="create"),
    # path("contact/<int:contact_id>/update/", views.contact, name="contact"),
    # path("contact/<int:contact_id>/delete/", views.contact, name="contact"),
]
