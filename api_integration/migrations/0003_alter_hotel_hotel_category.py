# Generated by Django 5.0.6 on 2024-06-20 22:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_integration', '0002_alter_hotel_options_alter_hotelcategory_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='hotel_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api_integration.hotelcategory'),
        ),
    ]
