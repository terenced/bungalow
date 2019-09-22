# Generated by Django 2.2.5 on 2019-09-22 19:28

from django.db import migrations, models
import django.db.models.deletion
import localflavor.us.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('bedrooms', models.IntegerField(default=0)),
                ('bathrooms', models.DecimalField(decimal_places=1, default=0.0, max_digits=4)),
                ('area_unit', models.CharField(choices=[('SqFt', 'Square Feet'), ('Mt', 'Metric')], default='SqFt', max_length=10)),
                ('home_size', models.IntegerField()),
                ('home_type', models.CharField(choices=[('Apartment', 'Apartment'), ('Condominium', 'Condominium'), ('Duplex', 'Duplex'), ('MultiFamily2To4', 'Multi Family (2 To 4)'), ('SingleFamily', 'Single Family'), ('VacantResidentialLand', 'Vacant Residential Land')], default='SingleFamily', max_length=100)),
                ('property_size', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', localflavor.us.models.USStateField(max_length=2)),
                ('zipcode', localflavor.us.models.USZipCodeField(max_length=10)),
                ('year_built', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Listings',
            },
        ),
        migrations.CreateModel(
            name='Metadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('external_id', models.CharField(max_length=200)),
                ('source', models.CharField(choices=[('zillow', 'Zillow'), ('internal', 'Internal')], default='internal', max_length=100)),
                ('external_link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='SalesHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sold_date', models.DateField()),
                ('sold_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Listing')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddIndex(
            model_name='metadata',
            index=models.Index(fields=['external_id'], name='core_metada_externa_77ade6_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='listing',
            unique_together={('address', 'city', 'state', 'zipcode')},
        ),
    ]