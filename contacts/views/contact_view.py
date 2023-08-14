from django.shortcuts import get_object_or_404, render

from contacts.models import Contact


def index(request):
    contacts = Contact.objects.filter(show=True).order_by("-id")
    context = {"contacts": contacts}

    return render(request, "contacts/index.html", context)


def contact(request, contact_id):
    # single_contact = Contact.objects.filter(pk=contact_id).first()
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)

    context = {"contact": single_contact}

    return render(request, "contacts/contact.html", context)
