# Generated by Django 5.0.3 on 2024-08-15 05:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0023_rename_balady_id_globalid_balady_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="QataryOfficeProject",
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
                ("global_id", models.IntegerField(blank=True, null=True)),
                (
                    "stage",
                    models.CharField(
                        choices=[
                            ("qatary", "Qatary"),
                            ("land_survey", "Land Survey"),
                            ("completed_land_survey", "Completed Land Survey"),
                            ("unofficial_transactions", "Unofficial Transactions"),
                        ],
                        max_length=100,
                    ),
                ),
                ("project_name", models.CharField(max_length=100)),
                (
                    "location_visit",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Working on it", "Working On It"),
                            ("Done", "Done"),
                            ("Hold", "Hold"),
                            ("Not required", "Not Required"),
                            ("ready", "Ready"),
                            ("no", "No"),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                ("location_visit_date", models.DateField(blank=True, null=True)),
                (
                    "record_number",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("status", models.CharField(blank=True, max_length=500, null=True)),
                (
                    "record_purpose",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "payment_status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Working on it", "Working On It"),
                            ("Done", "Done"),
                            ("Hold", "Hold"),
                            ("Not required", "Not Required"),
                            ("ready", "Ready"),
                            ("no", "No"),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "land_survey_issuance",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "client_phone",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="qatary_projects",
                        to="api.client",
                    ),
                ),
                (
                    "transaction_reviewer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="qatary_projects_reviewer",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
