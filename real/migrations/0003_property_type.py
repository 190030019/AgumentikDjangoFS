# Generated by Django 4.1.1 on 2022-11-08 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real', '0002_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='property_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]