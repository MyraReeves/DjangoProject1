# Generated by Django 5.1 on 2024-08-18 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('Dessert', 'Dessert'), ('Appetizer', 'Appetizer'), ('Entree', 'Entree'), ('Beverage', 'Beverage')], max_length=100),
        ),
    ]
