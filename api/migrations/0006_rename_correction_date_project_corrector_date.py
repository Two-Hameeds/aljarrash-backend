# Generated by Django 5.0.3 on 2024-05-20 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_modification_price_project_s_modification_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='correction_date',
            new_name='corrector_date',
        ),
    ]
