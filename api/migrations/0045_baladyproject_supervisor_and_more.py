# Generated by Django 5.0.3 on 2024-09-07 03:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0044_alter_attachment_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="baladyproject",
            name="supervisor",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="balady_supervisor",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="landsurveyproject",
            name="supervisor",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="land_survey_supervisor",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="qatariofficeproject",
            name="supervisor",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="qatari_supervisor",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="sortingdeedsproject",
            name="supervisor",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="sorting_deeds_supervisor",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="baladyproject",
            name="request_review",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Working on it", "Working On It"),
                    ("Done", "Done"),
                    ("Hold", "Hold"),
                    ("Not required", "Not Required"),
                    ("ready", "Ready"),
                    ("Post Tension", "Post Tension"),
                    ("no", "No"),
                ],
                max_length=100,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="baladyproject",
            name="technical_report",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Working on it", "Working On It"),
                    ("Done", "Done"),
                    ("Hold", "Hold"),
                    ("Not required", "Not Required"),
                    ("ready", "Ready"),
                    ("Post Tension", "Post Tension"),
                    ("no", "No"),
                ],
                max_length=255,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="designproject",
            name="architecture_status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Working on it", "Working On It"),
                    ("Done", "Done"),
                    ("Hold", "Hold"),
                    ("Not required", "Not Required"),
                    ("ready", "Ready"),
                    ("Post Tension", "Post Tension"),
                    ("no", "No"),
                ],
                max_length=100,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="designproject",
            name="electrical_status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Working on it", "Working On It"),
                    ("Done", "Done"),
                    ("Hold", "Hold"),
                    ("Not required", "Not Required"),
                    ("ready", "Ready"),
                    ("Post Tension", "Post Tension"),
                    ("no", "No"),
                ],
                max_length=100,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="designproject",
            name="plumbing_status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Working on it", "Working On It"),
                    ("Done", "Done"),
                    ("Hold", "Hold"),
                    ("Not required", "Not Required"),
                    ("ready", "Ready"),
                    ("Post Tension", "Post Tension"),
                    ("no", "No"),
                ],
                max_length=100,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="landsurveyproject",
            name="location_visit",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Working on it", "Working On It"),
                    ("Done", "Done"),
                    ("Hold", "Hold"),
                    ("Not required", "Not Required"),
                    ("ready", "Ready"),
                    ("Post Tension", "Post Tension"),
                    ("no", "No"),
                ],
                max_length=100,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="landsurveyproject",
            name="payment_status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Working on it", "Working On It"),
                    ("Done", "Done"),
                    ("Hold", "Hold"),
                    ("Not required", "Not Required"),
                    ("ready", "Ready"),
                    ("Post Tension", "Post Tension"),
                    ("no", "No"),
                ],
                max_length=100,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="qatariofficeproject",
            name="location_visit",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Working on it", "Working On It"),
                    ("Done", "Done"),
                    ("Hold", "Hold"),
                    ("Not required", "Not Required"),
                    ("ready", "Ready"),
                    ("Post Tension", "Post Tension"),
                    ("no", "No"),
                ],
                max_length=100,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="qatariofficeproject",
            name="payment_status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Working on it", "Working On It"),
                    ("Done", "Done"),
                    ("Hold", "Hold"),
                    ("Not required", "Not Required"),
                    ("ready", "Ready"),
                    ("Post Tension", "Post Tension"),
                    ("no", "No"),
                ],
                max_length=100,
                null=True,
            ),
        ),
    ]