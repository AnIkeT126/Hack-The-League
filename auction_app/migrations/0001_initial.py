# Generated by Django 3.2.2 on 2021-05-16 18:53

import auction_app.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('auction_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('auction_name', models.CharField(max_length=255)),
                ('auction_description', models.TextField()),
                ('auction_date', models.DateField(blank=True, validators=[auction_app.models.no_past])),
                ('auction_status', models.CharField(default='Pending', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('category_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='draftUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('dob', models.DateField(blank=True, validators=[auction_app.models.eighteenYears])),
                ('country', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=5)),
                ('address', models.CharField(max_length=255)),
                ('country_code', models.CharField(max_length=255)),
                ('contact', models.CharField(blank=True, max_length=255)),
                ('bank_account_number', models.IntegerField()),
                ('bank_sort_code', models.IntegerField()),
                ('client_type', models.CharField(max_length=255)),
                ('status', models.CharField(default='Pending', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_lot', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('artist_name', models.CharField(max_length=255)),
                ('production_year', models.PositiveIntegerField(default=2021, validators=[django.core.validators.MinValueValidator(1400), auction_app.models.max_value_current_year])),
                ('classification', models.CharField(choices=[('Landscape', 'Landscape'), ('Seascape', 'Seascape'), ('Portrait', 'Portrait'), ('Figure', 'Figure'), ('Still Life', 'Still Life'), ('Nude', 'Nude'), ('Animal', 'Animal'), ('Abstract', 'Abstract'), ('Other', 'Other')], max_length=255)),
                ('description', models.TextField()),
                ('estimated_price', models.CharField(max_length=255)),
                ('status', models.CharField(default='Pending', max_length=255)),
                ('auction', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='auction_app.auction')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='auction_app.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('dob', models.DateField(blank=True, validators=[auction_app.models.eighteenYears])),
                ('country', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=5)),
                ('address', models.CharField(max_length=255)),
                ('country_code', models.CharField(max_length=255)),
                ('contact', models.CharField(blank=True, max_length=255)),
                ('bank_account_number', models.IntegerField()),
                ('bank_sort_code', models.IntegerField()),
                ('client_type', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sculpture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(choices=[('Bronze', 'Bronze'), ('Marble', 'Marble'), ('Pewter', 'Pewter'), ('Other', 'Other')], max_length=255)),
                ('height', models.IntegerField()),
                ('length', models.IntegerField()),
                ('width', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('sculpture', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auction_app.item')),
            ],
        ),
        migrations.CreateModel(
            name='PhotographicImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Black', 'Black'), ('White', 'White')], max_length=255)),
                ('height', models.IntegerField()),
                ('length', models.IntegerField()),
                ('photographic_image', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auction_app.item')),
            ],
        ),
        migrations.CreateModel(
            name='Painting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medium', models.CharField(choices=[('Oil', 'Oil'), ('Acrylic', 'Acrylic'), ('Watercolor', 'Watercolor'), ('Other', 'Other')], max_length=255)),
                ('frame_status', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=255)),
                ('height', models.IntegerField()),
                ('length', models.IntegerField()),
                ('painting', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auction_app.item')),
            ],
        ),
        migrations.CreateModel(
            name='Drawing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medium', models.CharField(choices=[('Pencil', 'Pencil'), ('Ink', 'Ink'), ('Charcoal', 'Charcoal'), ('Other', 'Other')], max_length=255)),
                ('frame_status', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=255)),
                ('height', models.IntegerField()),
                ('length', models.IntegerField()),
                ('drawing', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auction_app.item')),
            ],
        ),
        migrations.CreateModel(
            name='Carving',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(choices=[('Oak', 'Oak'), ('Beach', 'Beach'), ('Pine', 'Pine'), ('Willow', 'Willow'), ('Other', 'Other')], max_length=255)),
                ('height', models.IntegerField()),
                ('length', models.IntegerField()),
                ('width', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('carving', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auction_app.item')),
            ],
        ),
    ]
