# Generated by Django 4.1.2 on 2023-02-10 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0013_alter_register_table_email_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='register_table',
        ),
    ]
