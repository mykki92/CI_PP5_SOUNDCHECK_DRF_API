# Generated by Django 3.2.23 on 2023-12-14 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='../soundcheck_default_post', upload_to='images/'),
        ),
    ]
