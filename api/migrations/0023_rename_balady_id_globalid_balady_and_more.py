# Generated by Django 5.0.3 on 2024-08-14 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0022_alter_attachment_type_alter_project_construction_eng"),
    ]

    operations = [
        migrations.RenameField(
            model_name="globalid",
            old_name="balady_id",
            new_name="balady",
        ),
        migrations.RenameField(
            model_name="globalid",
            old_name="design_id",
            new_name="design",
        ),
        migrations.RenameField(
            model_name="globalid",
            old_name="land_id",
            new_name="land",
        ),
        migrations.RenameField(
            model_name="globalid",
            old_name="sorting_id",
            new_name="sorting",
        ),
    ]