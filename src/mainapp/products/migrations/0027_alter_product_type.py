# Generated by Django 5.1 on 2024-08-19 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('Dessert', 'Dessert'), ('Beverage', 'Beverage'), ('Entree', 'Entree'), ('Appetizer', 'Appetizer')], max_length=100),
        ),
    ]
