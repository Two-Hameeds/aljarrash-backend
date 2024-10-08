# Generated by Django 5.0.3 on 2024-08-13 01:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0021_rename_global_uploaded_for_attachment_uploaded_for"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attachment",
            name="type",
            field=models.CharField(
                choices=[
                    ("deed", "Deed"),
                    ("license", "License"),
                    ("architecture_plan", "Architecture Plan"),
                    ("identity", "Identity"),
                    ("land_survey", "Land Survey"),
                    ("soil_test", "Soil Test"),
                    ("coordinate_certificate", "Coordinate Certificate"),
                    ("technical_report", "Technical Report"),
                    ("demolition_letters", "Demolition Letters"),
                    ("old_license", "Old License"),
                    ("civil_defense", "Civil Defense"),
                    ("construction_plan", "Construction Plan"),
                    ("energy_efficiency_plan", "Energy Efficiency Plan"),
                    ("building_pictures", "Building Pictures"),
                    ("container_contract", "Container Contract"),
                    ("other", "Other"),
                    ("contract", "Contract"),
                    ("report", "Report"),
                    ("plan", "Plan"),
                    ("old_plan", "Old Plan"),
                    ("load_bearing_certificate", "Load Bearing Certificate"),
                    ("location_certificate", "Location Certificate"),
                    ("autocad", "Autocad"),
                    ("client_form", "Client Form"),
                    ("water_authority", "Water Authority"),
                    ("electrical_plan", "Electrical Plan"),
                    ("plumbing_plan", "Plumbing Plan"),
                    ("complete_plans", "Complete Plans"),
                    ("request_purpose", "Request Purpose"),
                    ("determine_exert_type", "Determine Exert Type"),
                    ("standing_cutter_capacity", "Standing Cutter Capacity"),
                    (
                        "cutter_capacity_after_strengthening",
                        "Cutter Capacity After Strengthening",
                    ),
                    ("existing_loads", "Existing Loads"),
                    ("strengthening_reason", "Strengthening Reason"),
                    ("owner_sign_loads", "Owner Sign Loads"),
                    ("counter_location", "Counter Location"),
                    (
                        "coordinate_certificate_electricity",
                        "Coordinate Certificate Electricity",
                    ),
                    ("e_license", "E License"),
                    ("e_license_before_sort", "E License Before Sort"),
                    ("owner_authorize", "Owner Authorize"),
                    ("general_location", "General Location"),
                    ("facade_picture", "Facade Picture"),
                    ("approved_plan", "Approved Plan"),
                    ("electrical_service_card", "Electrical Service Card"),
                    ("spaces_table", "Spaces Table"),
                    ("approved_contractor", "Approved Contractor"),
                    ("engineering_supervision", "Engineering Supervision"),
                ],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="construction_eng",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="construction_engineer",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
