# Generated by Django 5.0.3 on 2024-08-20 14:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0035_alter_qataryofficeproject_global_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="baladyproject",
            name="global_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="api.globalid",
            ),
        ),
        migrations.AlterField(
            model_name="landsurveyproject",
            name="global_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="api.globalid",
            ),
        ),
        migrations.AlterField(
            model_name="qataryofficeproject",
            name="global_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="api.globalid",
            ),
        ),
        migrations.AlterField(
            model_name="sortingdeedsproject",
            name="global_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="api.globalid",
            ),
        ),
    ]