# Generated by Django 5.0.3 on 2024-08-20 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0036_alter_baladyproject_global_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="landsurveyproject",
            name="required_attachments",
            field=models.JSONField(blank=True, default=list, null=True),
        ),
        migrations.AddField(
            model_name="qataryofficeproject",
            name="required_attachments",
            field=models.JSONField(blank=True, default=list, null=True),
        ),
        migrations.AddField(
            model_name="sortingdeedsproject",
            name="required_attachments",
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]