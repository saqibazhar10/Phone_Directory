# Generated by Django 3.2.9 on 2021-12-09 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0006_alter_contact_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='img',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
