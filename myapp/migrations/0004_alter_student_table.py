# Generated by Django 4.2.4 on 2023-08-03 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_student_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='student',
            table='studentlist',
        ),
    ]
