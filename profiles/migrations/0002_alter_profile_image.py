# Generated by Django 3.2.23 on 2023-12-14 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../soundcheck_default_profile', upload_to='images/'),
        ),
    ]