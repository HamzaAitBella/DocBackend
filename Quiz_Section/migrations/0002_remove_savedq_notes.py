# Generated by Django 4.2.3 on 2023-09-02 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz_Section', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='savedq',
            name='notes',
        ),
    ]
