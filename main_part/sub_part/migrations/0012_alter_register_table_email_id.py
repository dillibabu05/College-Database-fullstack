# Generated by Django 4.1.2 on 2023-02-09 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0011_alter_register_table_email_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_table',
            name='email_id',
            field=models.EmailField(max_length=40, null=True),
        ),
    ]
