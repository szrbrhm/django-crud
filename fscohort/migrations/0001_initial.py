
# Generated by Django 3.2.8 on 2021-10-18 17:42


from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=154)),
                ('phone', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('1', 'Female'), ('2', 'Male'), ('3', 'Other'), ('4', 'Prefer Not Say')], max_length=50)),
                ('number', models.CharField(max_length=50)),
                ('image', models.ImageField(default='avatar.png', upload_to='student/')),
            ],
        ),
    ]
