# Generated by Django 4.0.4 on 2022-04-23 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flexistore', '0003_alter_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]