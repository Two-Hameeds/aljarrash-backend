# Generated by Django 5.0.3 on 2024-09-14 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0059_rename_deleted_from_baladyproject_delete_stage_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="supervisionproject",
            name="delete_stage",
            field=models.CharField(
                blank=True,
                choices=[
                    ("main", "Main"),
                    ("visit_supervision", "Visit Supervision"),
                    ("completed_supervision", "Completed Supervision"),
                    ("deleted_projects", "Deleted Projects"),
                ],
                max_length=100,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="supervisionproject",
            name="stage",
            field=models.CharField(
                choices=[
                    ("main", "Main"),
                    ("visit_supervision", "Visit Supervision"),
                    ("completed_supervision", "Completed Supervision"),
                    ("deleted_projects", "Deleted Projects"),
                ],
                max_length=100,
            ),
        ),
    ]
