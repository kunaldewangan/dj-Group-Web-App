# Generated by Django 2.2 on 2020-11-25 18:34

import accounts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='', max_length=6)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('phone_no', models.CharField(default='', max_length=12)),
                ('city', models.CharField(default='', max_length=250)),
                ('profile_picture', models.ImageField(blank=True, default='profile_picture/default_profile.png', upload_to=accounts.models.user_directory_path)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
