# Generated by Django 2.0 on 2018-06-03 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('his06', '0034_auto_20180603_1902'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicineKind',
            fields=[
                ('sm_id', models.CharField(db_column='sm_id', max_length=5, primary_key=True, serialize=False, verbose_name='药品种类ID')),
                ('sm_name', models.CharField(db_column='sm_name', max_length=255, verbose_name='药品种类名称')),
                ('me_id', models.ForeignKey(db_column='me_id', on_delete=django.db.models.deletion.DO_NOTHING, to='his06.MedicineType')),
            ],
        ),
        migrations.AlterField(
            model_name='patient',
            name='care_id',
            field=models.CharField(db_column='care_id_num', default='20180603763568', error_messages={0: '该诊疗卡号不存在'}, max_length=255, primary_key=True, serialize=False, verbose_name='诊疗卡号'),
        ),
    ]