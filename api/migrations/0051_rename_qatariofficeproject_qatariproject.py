# Generated by Django 5.0.3 on 2024-09-11 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0050_alter_supervisionproject_stage"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="QatariOfficeProject",
            new_name="QatariProject",
        ),
    ]
