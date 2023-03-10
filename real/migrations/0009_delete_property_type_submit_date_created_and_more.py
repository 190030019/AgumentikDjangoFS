# Generated by Django 4.1.1 on 2022-11-09 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real', '0008_submit'),
    ]

    operations = [
        migrations.DeleteModel(
            name='property_type',
        ),
        migrations.AddField(
            model_name='submit',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='submit',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='submit',
            name='status',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Failed', 'Failed')], max_length=100, null=True),
        ),
    ]
