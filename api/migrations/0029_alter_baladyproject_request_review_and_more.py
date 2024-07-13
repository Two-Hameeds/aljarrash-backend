# Generated by Django 5.0.3 on 2024-07-06 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_alter_comment_attachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baladyproject',
            name='request_review',
            field=models.CharField(blank=True, choices=[('Working on it', 'Working On It'), ('Done', 'Done'), ('Hold', 'Hold'), ('Not required', 'Not Required'), ('ready', 'Ready'), ('no', 'No')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='baladyproject',
            name='technical_report',
            field=models.CharField(blank=True, choices=[('Working on it', 'Working On It'), ('Done', 'Done'), ('Hold', 'Hold'), ('Not required', 'Not Required'), ('ready', 'Ready'), ('no', 'No')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='landsurveyproject',
            name='location_visit',
            field=models.CharField(blank=True, choices=[('Working on it', 'Working On It'), ('Done', 'Done'), ('Hold', 'Hold'), ('Not required', 'Not Required'), ('ready', 'Ready'), ('no', 'No')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='landsurveyproject',
            name='payment_status',
            field=models.CharField(blank=True, choices=[('Working on it', 'Working On It'), ('Done', 'Done'), ('Hold', 'Hold'), ('Not required', 'Not Required'), ('ready', 'Ready'), ('no', 'No')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='architecture_status',
            field=models.CharField(blank=True, choices=[('Working on it', 'Working On It'), ('Done', 'Done'), ('Hold', 'Hold'), ('Not required', 'Not Required'), ('ready', 'Ready'), ('no', 'No')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='electrical_status',
            field=models.CharField(blank=True, choices=[('Working on it', 'Working On It'), ('Done', 'Done'), ('Hold', 'Hold'), ('Not required', 'Not Required'), ('ready', 'Ready'), ('no', 'No')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='plumbing_status',
            field=models.CharField(blank=True, choices=[('Working on it', 'Working On It'), ('Done', 'Done'), ('Hold', 'Hold'), ('Not required', 'Not Required'), ('ready', 'Ready'), ('no', 'No')], max_length=100, null=True),
        ),
    ]