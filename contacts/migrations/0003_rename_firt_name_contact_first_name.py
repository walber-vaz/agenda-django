# Generated by Django 4.2.4 on 2023-08-11 18:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("contacts", "0002_alter_contact_description_alter_contact_email"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contact",
            old_name="firt_name",
            new_name="first_name",
        ),
    ]