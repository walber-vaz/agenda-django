from django.shortcuts import render

from contacts.models import Contact


def index(request):
    contacts = Contact.objects.all()
    context = {"contacts": contacts}

    return render(request, "contacts/index.html", context)
