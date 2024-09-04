# Generated by Django 5.0.3 on 2024-08-28 02:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0041_alter_baladyproject_stage_alter_designproject_stage_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ReceptionProject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("project_name", models.CharField(max_length=100)),
                ("notes", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "client_phone",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reception_projects",
                        to="api.client",
                    ),
                ),
                (
                    "global_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.globalid",
                    ),
                ),
            ],
        ),
    ]