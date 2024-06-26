# Generated by Django 5.0.3 on 2024-07-02 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_alter_comment_written_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='required_attachments',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='type',
            field=models.CharField(choices=[('contract', 'Contract'), ('deed', 'Deed'), ('report', 'Report'), ('identity', 'Identity'), ('container_contract', 'Containercontract'), ('license', 'License'), ('plan', 'Plan'), ('load_bearing_certificate', 'Loadbearingcertificate'), ('location_certificate', 'Locationcertificate'), ('land_survey', 'Landsurvey'), ('soil_test', 'Soiltest'), ('coordinate_certificate', 'Coordinatecertificate'), ('technical_report', 'Technicalreport'), ('demolition_letters', 'Demolitionletters'), ('autocad', 'Autocad'), ('client_form', 'Clientform'), ('old_license', 'Oldlicense'), ('civil_defense', 'Civildefense'), ('water_authority', 'Waterauthority'), ('construction_plan', 'Constructionplan'), ('electrical_plan', 'Electricalplan'), ('energy_efficiency_plan', 'Energyefficiencyplan'), ('plumbing_plan', 'Plumbingplan'), ('architecture_plan', 'Architectureplan'), ('other', 'Other')], max_length=100),
        ),
    ]
