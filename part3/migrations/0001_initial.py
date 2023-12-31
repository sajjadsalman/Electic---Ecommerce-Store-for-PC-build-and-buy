# Generated by Django 4.2.1 on 2023-06-21 06:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('HDD', 'HDD'), ('RAM', 'RAM'), ('OS', 'OS'), ('GPU', 'GPU'), ('CPU', 'CPU')], max_length=3)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('image_url', models.URLField(default='https://lh3.googleusercontent.com/RC4BS3P3PWp7cFviCPWButk0UFAxQKu54XayyjgzOSy2PTD0D9Zll1gSLaMzClmPNW8L3lvvg-2TeD857WIcoVSxC4G-Yo2Q7kUf_5TFuT66ZE5RvKWYykoVxDqe69f32vH6rt3m5A=w20')),
            ],
        ),
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image_url', models.URLField(default='https://lh3.googleusercontent.com/RC4BS3P3PWp7cFviCPWButk0UFAxQKu54XayyjgzOSy2PTD0D9Zll1gSLaMzClmPNW8L3lvvg-2TeD857WIcoVSxC4G-Yo2Q7kUf_5TFuT66ZE5RvKWYykoVxDqe69f32vH6rt3m5A=w20')),
                ('components', models.ManyToManyField(to='part3.component')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('computer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='part3.computer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
