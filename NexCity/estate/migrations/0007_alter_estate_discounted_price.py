# Generated by Django 4.2.5 on 2024-04-03 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0006_estate_c_of_o_estate_size_realtor_verified_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estate',
            name='discounted_price',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=100, null=True),
        ),
    ]
