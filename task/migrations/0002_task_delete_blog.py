# Generated by Django 5.0.6 on 2024-07-09 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_done', models.BooleanField(default=False, verbose_name='Bajarildi')),
                ('is_delete', models.BooleanField(default=False, verbose_name='Ochirildi')),
            ],
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
