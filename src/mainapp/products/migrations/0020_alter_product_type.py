# Generated by Django 5.1 on 2024-08-16 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('Entree', 'Entree'), ('Dessert', 'Dessert'), ('Beverage', 'Beverage'), ('Appetizer', 'Appetizer')], max_length=100),
        ),
    ]
