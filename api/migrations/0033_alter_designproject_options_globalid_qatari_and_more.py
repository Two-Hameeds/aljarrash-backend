# Generated by Django 5.0.3 on 2024-08-20 14:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0032_landsurveyproject_s_payments_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="designproject",
            options={"ordering": ["moved_at"]},
        ),
        migrations.AddField(
            model_name="globalid",
            name="qatari",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="api.qataryofficeproject",
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="written_for",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="comments",
                to="api.globalid",
            ),
        ),
    ]
