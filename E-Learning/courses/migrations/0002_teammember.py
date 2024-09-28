# Generated by Django 5.0.8 on 2024-09-28 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='team/')),
                ('linkedin', models.URLField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('github', models.URLField(blank=True)),
            ],
        ),
    ]
