# Generated by Django 3.2.6 on 2021-10-14 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_weightchange_date_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sugars',
        ),
    ]
