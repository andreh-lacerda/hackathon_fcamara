# Generated by Django 3.1.7 on 2021-03-29 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
