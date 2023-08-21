from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.shortcuts import render

from contacts.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = (
            "first_name",
            "last_name",
            "email",
            "phone",
            "description",
        )

    def clean(self):
        self.add_error(
            "first_name",
            ValidationError("First name is required", code="required"),
        )

        return super().clean()


def create(request):
    if request.method == "POST":
        context = {
            "form": ContactForm(data=request.POST or None),
        }

        return render(request, "contacts/create.html", context)

    context = {
        "form": ContactForm(),
    }

    return render(request, "contacts/create.html", context)
