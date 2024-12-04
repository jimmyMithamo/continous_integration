# Generated by Django 5.1.3 on 2024-12-04 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_order_order_date_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('RECEIVED', 'Received'), ('In transit', 'In transit'), ('COMPLETED', 'Completed'), ('CANCELED', 'Canceled')], default='RECEIVED', max_length=10),
        ),
    ]