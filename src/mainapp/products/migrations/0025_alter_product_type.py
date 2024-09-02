# Generated by Django 5.1 on 2024-08-18 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('Beverage', 'Beverage'), ('Entree', 'Entree'), ('Dessert', 'Dessert'), ('Appetizer', 'Appetizer')], max_length=100),
        ),
    ]
