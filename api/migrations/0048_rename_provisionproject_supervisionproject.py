# Generated by Django 5.0.3 on 2024-09-11 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0047_baladyproject_record_number_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="ProvisionProject",
            new_name="SupervisionProject",
        ),
    ]
