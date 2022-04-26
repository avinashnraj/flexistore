# Generated by Django 4.0.4 on 2022-04-23 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('uom_id', models.IntegerField()),
                ('price_per_unit', models.IntegerField()),
            ],
        ),
    ]
