# Generated by Django 5.0.3 on 2024-06-08 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_alter_project_client_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='current_stage',
            field=models.CharField(choices=[('sketch', 'Sketch'), ('sketch_review', 'Sketch Review'), ('approval_before_columns', 'Approval Before Columns'), ('awaiting_client_approval', 'Awaiting Client Approval'), ('execution_stage', 'Execution Stage'), ('autocad_review', 'Autocad Review'), ('ready_to_print', 'Ready To Print'), ('validate_sign_review_copy', 'Validate Sign Review Copy'), ('ready_to_collect', 'Ready To Collect'), ('client_received_copy', 'Client Received Copy'), ('edit_client_notes', 'Edit Client Notes'), ('license_issuance', 'License Issuance'), ('ready_for_final_receipt', 'Ready For Final Receipt'), ('completed_projects', 'Completed Projects'), ('inactive_projects', 'Inactive Projects')], max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='previous_stage',
            field=models.CharField(blank=True, choices=[('sketch', 'Sketch'), ('sketch_review', 'Sketch Review'), ('approval_before_columns', 'Approval Before Columns'), ('awaiting_client_approval', 'Awaiting Client Approval'), ('execution_stage', 'Execution Stage'), ('autocad_review', 'Autocad Review'), ('ready_to_print', 'Ready To Print'), ('validate_sign_review_copy', 'Validate Sign Review Copy'), ('ready_to_collect', 'Ready To Collect'), ('client_received_copy', 'Client Received Copy'), ('edit_client_notes', 'Edit Client Notes'), ('license_issuance', 'License Issuance'), ('ready_for_final_receipt', 'Ready For Final Receipt'), ('completed_projects', 'Completed Projects'), ('inactive_projects', 'Inactive Projects')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tableview',
            name='stage',
            field=models.CharField(choices=[('sketch', 'Sketch'), ('sketch_review', 'Sketch Review'), ('approval_before_columns', 'Approval Before Columns'), ('awaiting_client_approval', 'Awaiting Client Approval'), ('execution_stage', 'Execution Stage'), ('autocad_review', 'Autocad Review'), ('ready_to_print', 'Ready To Print'), ('validate_sign_review_copy', 'Validate Sign Review Copy'), ('ready_to_collect', 'Ready To Collect'), ('client_received_copy', 'Client Received Copy'), ('edit_client_notes', 'Edit Client Notes'), ('license_issuance', 'License Issuance'), ('ready_for_final_receipt', 'Ready For Final Receipt'), ('completed_projects', 'Completed Projects'), ('inactive_projects', 'Inactive Projects')], max_length=100),
        ),
    ]
