# Generated by Django 3.2.5 on 2021-11-23 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_orders_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='phone',
        ),
        migrations.AlterField(
            model_name='orders',
            name='address',
            field=models.CharField(max_length=111),
        ),
        migrations.AlterField(
            model_name='orders',
            name='city',
            field=models.CharField(max_length=111),
        ),
        migrations.AlterField(
            model_name='orders',
            name='email',
            field=models.CharField(max_length=111),
        ),
        migrations.AlterField(
            model_name='orders',
            name='name',
            field=models.CharField(max_length=90),
        ),
        migrations.AlterField(
            model_name='orders',
            name='state',
            field=models.CharField(max_length=111),
        ),
        migrations.AlterField(
            model_name='orders',
            name='zip_code',
            field=models.CharField(max_length=111),
        ),
    ]
