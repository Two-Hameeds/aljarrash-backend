# Generated by Django 5.0.3 on 2024-09-11 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0052_supervisionproject_required_attachments"),
    ]

    operations = [
        migrations.RenameField(
            model_name="globalid",
            old_name="provision",
            new_name="supervision",
        ),
    ]