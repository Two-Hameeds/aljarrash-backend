# Generated by Django 5.0.3 on 2024-05-20 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename__autocad_project_f_autocad_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='modification_price',
            new_name='s_modification_price',
        ),
    ]