# Generated by Django 4.2 on 2023-04-14 14:45

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
            name='Climb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.CharField(max_length=150)),
                ('user_climbed', models.BooleanField(default=False)),
                ('user_ticked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Crag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('description', models.CharField(max_length=400)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crag_type', to='chattclimbapi.crag')),
            ],
        ),
        migrations.CreateModel(
            name='CragType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Exposure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='HoldType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Steep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('steep', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conditions', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserTick',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('climb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved_climbs', to='chattclimbapi.climb')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_tick', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserSend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('climb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_climbs', to='chattclimbapi.climb')),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='climb_grade', to='chattclimbapi.grade')),
                ('hold_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='climb_hold_type', to='chattclimbapi.holdtype')),
                ('rating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='climb_rating', to='chattclimbapi.rating')),
                ('steep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='climb_steep', to='chattclimbapi.steep')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_send', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ape_index', models.FloatField()),
                ('birthday', models.DateField()),
                ('height', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_details', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProfilePic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile_picture', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CragImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('crag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chattclimbapi.crag')),
            ],
        ),
        migrations.CreateModel(
            name='ClimbMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('climb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='climb_videos', to='chattclimbapi.climb')),
            ],
        ),
        migrations.AddField(
            model_name='climb',
            name='crag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='climbs_crag', to='chattclimbapi.crag'),
        ),
        migrations.AddField(
            model_name='climb',
            name='grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='climbs_grade', to='chattclimbapi.grade'),
        ),
        migrations.AddField(
            model_name='climb',
            name='style',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='climbs_style', to='chattclimbapi.style'),
        ),
    ]
