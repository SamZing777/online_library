# Generated by Django 4.0.1 on 2022-01-15 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['first_name']},
        ),
        migrations.AddField(
            model_name='author',
            name='title',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]