# Generated by Django 5.1 on 2024-08-15 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('Beverage', 'Beverage'), ('Appetizer', 'Appetizer'), ('Dessert', 'Dessert'), ('Entree', 'Entree')], max_length=100),
        ),
    ]
