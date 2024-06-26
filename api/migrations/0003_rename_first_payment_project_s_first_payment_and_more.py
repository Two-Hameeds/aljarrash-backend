# Generated by Django 5.0.3 on 2024-05-19 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_project_value_project_s_project_value'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='first_payment',
            new_name='s_first_payment',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='first_payment_date',
            new_name='s_first_payment_date',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='first_payment_stage',
            new_name='s_first_payment_stage',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='second_payment',
            new_name='s_second_payment',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='second_payment_date',
            new_name='s_second_payment_date',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='second_payment_stage',
            new_name='s_second_payment_stage',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='third_payment',
            new_name='s_third_payment',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='third_payment_date',
            new_name='s_third_payment_date',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='third_payment_stage',
            new_name='s_third_payment_stage',
        ),
    ]
