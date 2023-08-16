from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

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


def search(request):
    query = request.GET.get("q", "").strip()

    if query == "" or len(query) <= 0:
        return redirect("contacts:index")

    contacts = (
        Contact.objects.filter(
            Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
            | Q(email__icontains=query)
            | Q(phone__icontains=query)
        )
        .filter(show=True)
        .order_by("-id")
    )

    context = {"contacts": contacts}

    return render(request, "contacts/index.html", context)
