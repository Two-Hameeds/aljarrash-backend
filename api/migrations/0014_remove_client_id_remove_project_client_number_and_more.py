# Generated by Django 5.0.3 on 2024-06-08 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_attachment_attachment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='id',
        ),
        migrations.RemoveField(
            model_name='project',
            name='client_number',
        ),
        migrations.RemoveField(
            model_name='project',
            name='typeof_follow_up',
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(max_length=13, primary_key=True, serialize=False),
        ),
    ]
