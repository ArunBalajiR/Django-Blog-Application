# Generated by Django 3.0.5 on 2020-06-09 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200609_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='Default.jpg', upload_to='profile_pics'),
        ),
    ]
