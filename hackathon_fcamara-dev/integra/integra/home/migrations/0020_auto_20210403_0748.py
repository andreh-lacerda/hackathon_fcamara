# Generated by Django 3.1.7 on 2021-04-03 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20210401_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.school'),
        ),
    ]
