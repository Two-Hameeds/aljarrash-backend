# Generated by Django 5.0.3 on 2024-08-20 23:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0038_rename_qataryofficeproject_qatariofficeproject"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attachment",
            name="uploaded_for",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="attachments",
                to="api.globalid",
            ),
        ),
    ]
