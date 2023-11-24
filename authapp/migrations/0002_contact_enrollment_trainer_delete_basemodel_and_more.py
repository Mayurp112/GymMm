# Generated by Django 4.2.7 on 2023-11-24 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.CharField(max_length=12)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=25)),
                ('Email', models.EmailField(max_length=254)),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('PhoneNumber', models.CharField(max_length=12)),
                ('DOB', models.DateField(max_length=8)),
                ('Address', models.TextField()),
                ('PaymentStatus', models.CharField(blank=True, max_length=55, null=True)),
                ('Price', models.IntegerField(blank=True, max_length=55, null=True)),
                ('DueDate', models.DateField(blank=True, null=True)),
                ('TimeStamp', models.DateField(auto_now_add=True)),
                ('SelectMembershipplan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authapp.membershipplan')),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=55)),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('PhoneNumber', models.CharField(max_length=12)),
            ],
        ),
        migrations.DeleteModel(
            name='BaseModel',
        ),
        migrations.AlterField(
            model_name='gallery',
            name='img',
            field=models.ImageField(upload_to='gallery'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='SelectTrainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authapp.trainer'),
        ),
    ]