# Generated by Django 5.0.3 on 2024-08-20 05:44

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0030_remove_baladyproject_s_history_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="landsurveyproject",
            options={"ordering": ["moved_at"]},
        ),
        migrations.AlterModelOptions(
            name="qataryofficeproject",
            options={"ordering": ["moved_at"]},
        ),
        migrations.AlterModelOptions(
            name="sortingdeedsproject",
            options={"ordering": ["moved_at"]},
        ),
        migrations.RemoveField(
            model_name="payment",
            name="s_history",
        ),
        migrations.AddField(
            model_name="landsurveyproject",
            name="moved_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="qataryofficeproject",
            name="moved_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="sortingdeedsproject",
            name="moved_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="History",
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
                ("action", models.CharField(max_length=100)),
                ("stage", models.CharField(blank=True, max_length=100, null=True)),
                ("new_stage", models.CharField(blank=True, max_length=100, null=True)),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]