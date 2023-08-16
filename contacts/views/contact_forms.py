# from django.core.paginator import Paginator

# from contacts.models import Contact

# from django.db.models import Q
# from django.shortcuts import get_object_or_404, redirect, render


from django.shortcuts import render


def create(request):
    # contacts = Contact.objects.filter(show=True).order_by("-id")
    # paginator = Paginator(contacts, 10)
    # page_number = request.GET.get("page")
    # page_obj = paginator.get_page(page_number)
    context = {}

    return render(request, "contacts/create.html", context)
