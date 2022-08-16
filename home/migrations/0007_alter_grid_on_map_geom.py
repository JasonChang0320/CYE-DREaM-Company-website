# Generated by Django 4.0.6 on 2022-08-01 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_grid_on_map_geom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grid_on_map',
            name='geom',
            field=models.JSONField(verbose_name={'features': [{'geometry': {'coordinates': [[[120.06958007812499, 24.632038149596895], [120.9649658203125, 24.632038149596895], [120.9649658203125, 25.46311452925943], [120.06958007812499, 25.46311452925943], [120.06958007812499, 24.632038149596895]]], 'type': 'Polygon'}, 'properties': {'name': '1'}, 'type': 'Feature'}, {'geometry': {'coordinates': [[[120.970458984375, 24.627044746156027], [121.871337890625, 24.627044746156027], [121.871337890625, 25.468073997498134], [120.970458984375, 25.468073997498134], [120.970458984375, 24.627044746156027]]], 'type': 'Polygon'}, 'properties': {'name': '2'}, 'type': 'Feature'}, {'geometry': {'coordinates': [[[120.05310058593749, 23.83560098662095], [120.9649658203125, 23.83560098662095], [120.9649658203125, 24.612063338963782], [120.05310058593749, 24.612063338963782], [120.05310058593749, 23.83560098662095]]], 'type': 'Polygon'}, 'properties': {'name': '3'}, 'type': 'Feature'}, {'geometry': {'coordinates': [[[120.97595214843749, 23.85569800975124], [121.86035156249999, 23.85569800975124], [121.86035156249999, 24.617057340809524], [120.97595214843749, 24.617057340809524], [120.97595214843749, 23.85569800975124]]], 'type': 'Polygon'}, 'properties': {'name': '4'}, 'type': 'Feature'}, {'geometry': {'coordinates': [[[120.0640869140625, 23.185813175302915], [120.9649658203125, 23.185813175302915], [120.9649658203125, 23.83560098662095], [120.0640869140625, 23.83560098662095], [120.0640869140625, 23.185813175302915]]], 'type': 'Polygon'}, 'properties': {'name': '5'}, 'type': 'Feature'}, {'geometry': {'coordinates': [[[120.970458984375, 23.19086257687362], [121.84936523437499, 23.19086257687362], [121.84936523437499, 23.85067404608915], [120.970458984375, 23.85067404608915], [120.970458984375, 23.19086257687362]]], 'type': 'Polygon'}, 'properties': {'name': '6'}, 'type': 'Feature'}, {'geometry': {'coordinates': [[[120.0640869140625, 22.421184710331858], [120.9649658203125, 22.421184710331858], [120.9649658203125, 23.183288403039526], [120.0640869140625, 23.183288403039526], [120.0640869140625, 22.421184710331858]]], 'type': 'Polygon'}, 'properties': {'name': '7'}, 'type': 'Feature'}, {'geometry': {'coordinates': [[[120.96771240234375, 22.421184710331858], [121.86584472656251, 22.421184710331858], [121.86584472656251, 23.1959117878095], [120.96771240234375, 23.1959117878095], [120.96771240234375, 22.421184710331858]]], 'type': 'Polygon'}, 'properties': {'name': '8'}, 'type': 'Feature'}, {'geometry': {'coordinates': [[[120.06958007812499, 21.87679231243837], [120.96771240234375, 21.87679231243837], [120.96771240234375, 22.41356763836979], [120.06958007812499, 22.41356763836979], [120.06958007812499, 21.87679231243837]]], 'type': 'Polygon'}, 'properties': {'name': '9'}, 'type': 'Feature'}, {'geometry': {'coordinates': [[[120.96771240234375, 21.88188980762927], [121.86859130859375, 21.88188980762927], [121.86859130859375, 22.41356763836979], [120.96771240234375, 22.41356763836979], [120.96771240234375, 21.88188980762927]]], 'type': 'Polygon'}, 'properties': {'name': '10'}, 'type': 'Feature'}], 'type': 'FeatureCollection'}),
        ),
    ]