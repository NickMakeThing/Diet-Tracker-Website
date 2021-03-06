# Generated by Django 3.2.6 on 2021-08-23 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210821_0656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='carb',
        ),
        migrations.AddField(
            model_name='product',
            name='carbs',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='current_weight',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='energy',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='fat',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='protein',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='sugars',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='weightchange',
            name='weight_change',
            field=models.FloatField(),
        ),
    ]
