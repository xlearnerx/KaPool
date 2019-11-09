# Generated by Django 2.2.5 on 2019-11-09 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191103_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(blank=True, help_text='Date of birth', null=True, verbose_name='Date of birth'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('female', 'Female'), ('male', 'Male'), ('wont-say', "Won't say")], default='wont-say', help_text="User's gender", max_length=30, null=True, verbose_name='Gender'),
        ),
    ]
