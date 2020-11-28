# Generated by Django 2.2 on 2020-11-27 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['user__username']},
        ),
        migrations.AddField(
            model_name='profile',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('-', '-'), ('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='-', max_length=6),
        ),
    ]
