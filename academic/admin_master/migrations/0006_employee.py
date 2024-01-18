# Generated by Django 4.2.7 on 2024-01-03 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_master', '0005_qualification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empname', models.CharField(max_length=200)),
                ('emparea', models.CharField(max_length=200)),
                ('status', models.IntegerField(default=1)),
            ],
        ),
    ]