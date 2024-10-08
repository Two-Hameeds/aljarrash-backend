# Generated by Django 5.0.3 on 2024-09-11 21:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0054_visit"),
    ]

    operations = [
        migrations.AddField(
            model_name="visit",
            name="visited_for",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="visits",
                to="api.globalid",
            ),
            preserve_default=False,
        ),
    ]
