# Generated by Django 5.0.3 on 2024-07-04 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_remove_baladyproject_architect_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baladyproject',
            name='path',
            field=models.CharField(choices=[('balady', 'Balady'), ('service_card', 'Service Card'), ('quantity_sorting', 'Quantity Sorting')], max_length=100),
        ),
    ]