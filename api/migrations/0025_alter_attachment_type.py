# Generated by Django 5.0.3 on 2024-07-02 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_project_required_attachments_alter_attachment_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='type',
            field=models.CharField(choices=[('contract', 'Contract'), ('deed', 'Deed'), ('report', 'Report'), ('identity', 'Identity'), ('container_contract', 'Containercontract'), ('license', 'License'), ('plan', 'Plan'), ('load_bearing_certificate', 'Loadbearingcertificate'), ('location_certificate', 'Locationcertificate'), ('land_survey', 'Landsurvey'), ('soil_test', 'Soiltest'), ('coordinate_certificate', 'Coordinatecertificate'), ('technical_report', 'Technicalreport'), ('demolition_letters', 'Demolitionletters'), ('autocad', 'Autocad'), ('client_form', 'Clientform'), ('old_license', 'Oldlicense'), ('civil_defense', 'Civildefense'), ('water_authority', 'Waterauthority'), ('construction_plan', 'Constructionplan'), ('electrical_plan', 'Electricalplan'), ('energy_efficiency_plan', 'Energyefficiencyplan'), ('plumbing_plan', 'Plumbingplan'), ('architecture_plan', 'Architectureplan'), ('building_pictures', 'Buildingpictures'), ('other', 'Other')], max_length=100),
        ),
    ]
