# Generated by Django 4.1.2 on 2023-02-09 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0010_alter_register_table_email_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_table',
            name='email_id',
            field=models.EmailField(max_length=40),
        ),
        migrations.AlterField(
            model_name='register_table',
            name='profile_picture',
            field=models.ImageField(upload_to='documents'),
        ),
    ]
