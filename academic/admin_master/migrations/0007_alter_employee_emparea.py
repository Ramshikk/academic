# Generated by Django 4.2.7 on 2024-01-03 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_master', '0006_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emparea',
            field=models.IntegerField(choices=[(1, 'Accountant'), (2, 'Teacher'), (3, 'cafteria'), (4, 'Librarian'), (5, 'Others')]),
        ),
    ]