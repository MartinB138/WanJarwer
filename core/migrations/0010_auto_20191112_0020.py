# Generated by Django 2.2.6 on 2019-11-12 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20191111_2312'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca_Gab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Marca_Graph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='gab',
            name='marca_gabinete',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Marca_Gab'),
        ),
        migrations.AlterField(
            model_name='graph',
            name='graph',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Marca_Graph'),
        ),
    ]