# Generated by Django 2.2.1 on 2019-06-17 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='bukuke',
        ),
        migrations.AddField(
            model_name='post',
            name='konten',
            field=models.TextField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='judul',
            field=models.CharField(max_length=255),
        ),
    ]