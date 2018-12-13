# Generated by Django 2.0.6 on 2018-12-19 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0011_auto_20181210_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='monthly_pages',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='monthly_requests',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='number_pages',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='number_requests',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='pages_per_month',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='requests_per_month',
        ),
        migrations.AlterField(
            model_name='organization',
            name='date_update',
            field=models.DateField(blank=True, help_text='Date when monthly requests are restored', null=True, verbose_name='date update'),
        ),
    ]