# Generated by Django 5.1 on 2024-08-31 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopApp', '0003_alter_orders_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='kg',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
