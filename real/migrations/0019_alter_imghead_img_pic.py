# Generated by Django 4.1.1 on 2023-01-23 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real', '0018_alter_imghead_img_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imghead',
            name='img_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images1/'),
        ),
    ]