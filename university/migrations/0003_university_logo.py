# Generated by Django 4.1.2 on 2022-11-02 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0002_rename_acceptancerate_university_acceptance_rate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='imags/'),
        ),
    ]