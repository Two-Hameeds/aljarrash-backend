# Generated by Django 5.0.3 on 2024-08-20 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0029_rename_project_designproject_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="baladyproject",
            name="s_history",
        ),
        migrations.RemoveField(
            model_name="designproject",
            name="s_history",
        ),
        migrations.AlterField(
            model_name="sortingdeedsproject",
            name="stage",
            field=models.CharField(
                choices=[
                    ("land_sorting", "Land Sorting"),
                    ("land_merging", "Land Merging"),
                    ("housing_sorting", "Housing Sorting"),
                    ("completed_land_sorting", "Completed Land Sorting"),
                    ("completed_land_merging", "Completed Land Merging"),
                    ("completed_housing_sorting", "Completed Housing Sorting"),
                ],
                max_length=100,
            ),
        ),
    ]