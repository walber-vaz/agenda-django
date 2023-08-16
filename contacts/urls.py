from django.urls import path

from contacts import views

app_name = "contacts"

urlpatterns = [
    path("<int:contact_id>/", views.contact, name="contact"),
    path("search/", views.search, name="search"),
    path("", views.index, name="index"),
]
