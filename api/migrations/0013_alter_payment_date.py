# Generated by Django 5.0.3 on 2024-08-03 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0012_alter_project_global_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="date",
            field=models.DateField(blank=True),
        ),
    ]