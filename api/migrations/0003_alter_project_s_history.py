# Generated by Django 5.0.3 on 2024-07-23 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_rename_architecture_reviewer_project_architect_reviewer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="s_history",
            field=models.JSONField(blank=True, default=[], null=True),
        ),
    ]
