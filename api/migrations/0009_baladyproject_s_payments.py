# Generated by Django 5.0.3 on 2024-08-03 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0008_rename_path_baladyproject_stage_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="baladyproject",
            name="s_payments",
            field=models.JSONField(default=list),
        ),
    ]
