# Generated by Django 2.0 on 2018-06-09 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('his06', '0042_auto_20180609_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='care_id',
            field=models.CharField(db_column='care_id_num', default='20180609129646', error_messages={0: '该诊疗卡号不存在'}, max_length=255, primary_key=True, serialize=False, verbose_name='诊疗卡号'),
        ),
    ]