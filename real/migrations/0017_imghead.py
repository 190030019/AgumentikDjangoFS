# Generated by Django 4.1.1 on 2023-01-23 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real', '0016_rename_contact_contact_us'),
    ]

    operations = [
        migrations.CreateModel(
            name='imghead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_pic', models.ImageField(blank=True, default='profile1.jpg', null=True, upload_to='')),
            ],
        ),
    ]