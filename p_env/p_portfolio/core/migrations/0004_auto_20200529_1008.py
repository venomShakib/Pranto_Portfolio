# Generated by Django 3.0.6 on 2020-05-29 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_aboutme'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='career')),
            ],
            options={
                'verbose_name': 'My career',
                'verbose_name_plural': 'My career',
            },
        ),
        migrations.AlterModelOptions(
            name='aboutme',
            options={'verbose_name': 'About me', 'verbose_name_plural': 'About Me'},
        ),
    ]
