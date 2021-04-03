# Generated by Django 3.1.7 on 2021-03-30 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20210330_0935'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ListItem',
            new_name='List',
        ),
        migrations.AddField(
            model_name='item',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='itemselection',
            name='item_quantity',
            field=models.IntegerField(default=0),
        ),
    ]
