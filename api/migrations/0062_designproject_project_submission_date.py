# Generated by Django 5.0.3 on 2024-09-23 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0061_alter_baladyproject_delete_stage_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="designproject",
            name="project_submission_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]