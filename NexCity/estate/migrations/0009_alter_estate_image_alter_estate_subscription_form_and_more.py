# Generated by Django 4.2.5 on 2024-04-04 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0008_alter_estate_image_alter_estate_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estate',
            name='image',
            field=models.ImageField(blank=True, default='\\image\\pexels-pixabay-280221.jpg', null=True, upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='estate',
            name='subscription_form',
            field=models.FileField(blank=True, default='\\image\\pexels-pixabay-280221.jpg', null=True, upload_to='subscription/'),
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('email', models.CharField(max_length=400)),
                ('contact', models.CharField(max_length=400)),
                ('address', models.TextField()),
                ('paid', models.BooleanField(default=False)),
                ('state', models.CharField(max_length=400)),
                ('estate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estate.estate')),
            ],
        ),
    ]
