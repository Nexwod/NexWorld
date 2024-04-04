# Generated by Django 4.2.5 on 2024-04-03 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0007_alter_estate_discounted_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estate',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='estate',
            name='size',
            field=models.IntegerField(default='465', null=True),
        ),
        migrations.AlterField(
            model_name='estate',
            name='subscription_form',
            field=models.FileField(blank=True, null=True, upload_to='subscription/'),
        ),
    ]