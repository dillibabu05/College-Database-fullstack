# Generated by Django 4.1.2 on 2023-02-09 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0012_alter_register_table_email_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_table',
            name='email_id',
            field=models.EmailField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]