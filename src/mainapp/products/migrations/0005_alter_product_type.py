# Generated by Django 5.1 on 2024-08-11 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('Appetizer', 'Appetizer'), ('Beverage', 'Beverage'), ('Dessert', 'Dessert'), ('Entree', 'Entree')], max_length=100),
        ),
    ]
