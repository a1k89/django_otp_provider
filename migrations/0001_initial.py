# Generated by Django 3.2.4 on 2021-09-09 09:24

from django.db import migrations, models
import django_otp_provider.django_otp_provider.utils
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Otp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('key', models.CharField(max_length=50, unique=True, validators=[django_otp_provider.django_otp_provider.utils.Transport.validator])),
                ('expire_at', models.DateTimeField(default=django_otp_provider.django_otp_provider.utils.expire_at)),
                ('attempts', models.PositiveIntegerField(default=3)),
                ('is_code_sended', models.BooleanField(default=False)),
            ],
            options={
                'unique_together': {('token', 'key')},
            },
        ),
    ]
