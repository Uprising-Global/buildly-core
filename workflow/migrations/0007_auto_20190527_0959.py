# Generated by Django 2.2.1 on 2019-05-27 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0006_auto_20190514_1158'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workflowleveltype',
            options={'ordering': ('create_date',)},
        ),
    ]