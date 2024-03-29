# Generated by Django 3.2.5 on 2021-09-12 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_modelcompany_custid'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelInvoice',
            fields=[
                ('invoice_id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('month', models.DateField()),
                ('ispaid', models.BooleanField(blank=True, null=True)),
                ('customer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.modelcustomer')),
            ],
        ),
    ]
