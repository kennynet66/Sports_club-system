# Generated by Django 4.2.2 on 2023-08-01 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_sports_details_alter_member_details_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member_details',
            name='school_of_origin',
            field=models.CharField(choices=[('guardian', 'Guardian'), ('mother', 'Mother'), ('father', 'Father')], default=None, max_length=20),
        ),
    ]
