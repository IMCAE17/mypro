 # Generated by Django 4.2.4 on 2023-08-02 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='address',
            new_name='Address',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='marks',
            new_name='Marks',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='name',
            new_name='Name',
        ),
    ]
