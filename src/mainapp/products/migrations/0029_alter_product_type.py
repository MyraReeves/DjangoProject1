# Generated by Django 5.1 on 2024-08-20 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0028_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('Entree', 'Entree'), ('Beverage', 'Beverage'), ('Dessert', 'Dessert'), ('Appetizer', 'Appetizer')], max_length=100),
        ),
    ]
