# Generated by Django 5.1 on 2024-08-16 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('Appetizer', 'Appetizer'), ('Dessert', 'Dessert'), ('Beverage', 'Beverage'), ('Entree', 'Entree')], max_length=100),
        ),
    ]
