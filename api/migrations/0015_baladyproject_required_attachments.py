# Generated by Django 5.0.3 on 2024-08-04 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0014_alter_payment_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="baladyproject",
            name="required_attachments",
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]
