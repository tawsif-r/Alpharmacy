# Generated by Django 4.2 on 2023-04-28 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100, null=True)),
                ('customer_phone', models.PositiveIntegerField(null=True)),
                ('customer_mail', models.CharField(max_length=100, null=True)),
                ('customer_age', models.PositiveIntegerField(null=True)),
                ('customer_password', models.CharField(max_length=100, null=True)),
                ('customer_location', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(max_length=100, null=True)),
                ('expire_date', models.DateField(null=True)),
                ('group_name', models.CharField(max_length=100, null=True)),
                ('company_name', models.CharField(max_length=100, null=True)),
                ('price', models.PositiveIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pharmacy_owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=100, null=True)),
                ('owner_phonenumber', models.PositiveIntegerField(null=True)),
                ('owner_password', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pharmacy_name', models.CharField(max_length=100, null=True)),
                ('pharmacy_location', models.CharField(max_length=100, null=True)),
                ('pharmacy_owner', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='pharmacy_app.pharmacy_owner')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_bill', models.PositiveIntegerField(null=True)),
                ('quantity', models.PositiveIntegerField(null=True)),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], max_length=100, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pharmacy_app.customer')),
                ('medicine', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pharmacy_app.medicine')),
            ],
        ),
    ]
