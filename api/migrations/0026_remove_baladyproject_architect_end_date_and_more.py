# Generated by Django 5.0.3 on 2024-07-03 03:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_alter_attachment_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baladyproject',
            name='architect_end_date',
        ),
        migrations.RemoveField(
            model_name='baladyproject',
            name='architect_start_date',
        ),
        migrations.RemoveField(
            model_name='baladyproject',
            name='architecture_status',
        ),
        migrations.RemoveField(
            model_name='baladyproject',
            name='columns_approval_date',
        ),
        migrations.RemoveField(
            model_name='baladyproject',
            name='construction_end_date',
        ),
        migrations.RemoveField(
            model_name='baladyproject',
            name='construction_eng',
        ),
        migrations.RemoveField(
            model_name='baladyproject',
            name='construction_review',
        ),
        migrations.RemoveField(
            model_name='baladyproject',
            name='construction_start_date',
        ),
        migrations.RemoveField(
            model_name='baladyproject',
            name='construction_status',
        ),
        migrations.RemoveField(
            model_name='baladyproject',
            name='design_eng',
        ),
        migrations.RemoveField(
            model_name='baladyproject',
            name='electrical_end_date',
        ),
        migrations.RemoveField(
            model_name='baladyproject',
            name='electrical_eng',
        ),
        migrations.RemoveField(
            model_name='baladyproject',
            name='electrical_start_date',
        ),
        migrations.RemoveField(
            model_name='baladyproject',
            name='electrical_status',
        ),
        migrations.RemoveField(
            model_name='baladyproject',
            name='investor_affiliation',
        ),
        migrations.RemoveField(
            model_name='baladyproject',
            name='land_area',
        ),
        migrations.RemoveField(
            model_name='baladyproject',
            name='land_number',
        ),
        migrations.RemoveField(
            model_name='baladyproject',
            name='plan_delivery_date',
        ),
        migrations.RemoveField(
            model_name='baladyproject',
            name='plumbing_end_date',
        ),
        migrations.RemoveField(
            model_name='baladyproject',
            name='plumbing_start_date',
        ),
        migrations.RemoveField(
            model_name='baladyproject',
            name='plumbing_status',
        ),
        migrations.RemoveField(
            model_name='baladyproject',
            name='project_location',
        ),
        migrations.RemoveField(
            model_name='baladyproject',
            name='project_number',
        ),
        migrations.RemoveField(
            model_name='baladyproject',
            name='project_receipt_date',
        ),
        migrations.RemoveField(
            model_name='baladyproject',
            name='project_type',
        ),
        migrations.RemoveField(
            model_name='baladyproject',
            name='request_status',
        ),
        migrations.RemoveField(
            model_name='baladyproject',
            name='sketch_approval_date',
        ),
        migrations.RemoveField(
            model_name='baladyproject',
            name='sketch_progress',
        ),
        migrations.RemoveField(
            model_name='baladyproject',
            name='stage',
        ),
        migrations.AddField(
            model_name='baladyproject',
            name='approval_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='baladyproject',
            name='building_inspection_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='baladyproject',
            name='design_proj',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='balady_project', to='api.project'),
        ),
        migrations.AddField(
            model_name='baladyproject',
            name='is_eng_needed',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='baladyproject',
            name='municipality_visit',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='baladyproject',
            name='path',
            field=models.CharField(choices=[('balady', 'Balady'), ('service_card', 'Service Card'), ('Quantity_Sorting', 'Quantity Sorting')], default='balady', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='baladyproject',
            name='request_ready_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='baladyproject',
            name='request_review',
            field=models.CharField(blank=True, choices=[('Working on it', 'Working On It'), ('Done', 'Done'), ('Hold', 'Hold'), ('Not required', 'Not Required'), ('Ready', 'Ready'), ('No', 'No')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='baladyproject',
            name='request_submission',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='baladyproject',
            name='request_type',
            field=models.CharField(choices=[('issue_license', 'Issue License'), ('convert_license_to_electronic', 'Convert License To Electronic'), ('restoration_license', 'Restoration License'), ('add_modify_components_license', 'Add Modify Components License'), ('construction_completion_certificate', 'Construction Completion Certificate'), ('license_separation', 'License Separation'), ('license_renewal', 'License Renewal'), ('demolition_license', 'Demolition License'), ('ownership_license_transfer', 'Ownership License Transfer'), ('survey_decision', 'Survey Decision'), ('service_card', 'Service Card'), ('loading_certificate', 'Loading Certificate'), ('components_form', 'Components Form'), ('quantity_sorting', 'Quantity Sorting')], default='issue_license', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='baladyproject',
            name='sorting_purpose',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='baladyproject',
            name='technical_report',
            field=models.CharField(blank=True, choices=[('Working on it', 'Working On It'), ('Done', 'Done'), ('Hold', 'Hold'), ('Not required', 'Not Required'), ('Ready', 'Ready'), ('No', 'No')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='baladyproject',
            name='transaction_stop_reason',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='landsurveyproject',
            name='location_visit',
            field=models.CharField(blank=True, choices=[('Working on it', 'Working On It'), ('Done', 'Done'), ('Hold', 'Hold'), ('Not required', 'Not Required'), ('Ready', 'Ready'), ('No', 'No')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='landsurveyproject',
            name='payment_status',
            field=models.CharField(blank=True, choices=[('Working on it', 'Working On It'), ('Done', 'Done'), ('Hold', 'Hold'), ('Not required', 'Not Required'), ('Ready', 'Ready'), ('No', 'No')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='architecture_status',
            field=models.CharField(blank=True, choices=[('Working on it', 'Working On It'), ('Done', 'Done'), ('Hold', 'Hold'), ('Not required', 'Not Required'), ('Ready', 'Ready'), ('No', 'No')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='electrical_status',
            field=models.CharField(blank=True, choices=[('Working on it', 'Working On It'), ('Done', 'Done'), ('Hold', 'Hold'), ('Not required', 'Not Required'), ('Ready', 'Ready'), ('No', 'No')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='plumbing_status',
            field=models.CharField(blank=True, choices=[('Working on it', 'Working On It'), ('Done', 'Done'), ('Hold', 'Hold'), ('Not required', 'Not Required'), ('Ready', 'Ready'), ('No', 'No')], max_length=100, null=True),
        ),
    ]
