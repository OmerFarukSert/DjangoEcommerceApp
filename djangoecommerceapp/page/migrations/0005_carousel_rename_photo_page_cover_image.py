# Generated by Django 4.1 on 2023-03-05 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_alter_page_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameField(
            model_name='page',
            old_name='photo',
            new_name='cover_image',
        ),
    ]
