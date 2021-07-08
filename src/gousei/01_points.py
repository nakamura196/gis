import shutil
from osgeo import gdal, osr
import json
import csv
import re

import pyproj
import csv 

wgs84=pyproj.CRS("EPSG:4326")
jgd2011_9 = pyproj.CRS("EPSG:3857")


def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

width = 43890
height = 38875

arr = []

with open('map.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) == 0:
            continue
        arr.append({
            "label" : row[0],
            "value" : (row[1])
        })

print(arr)

max_size = max(width, height)

r = 6000 / max_size

print(r)

rows = []
rows.append(["mapX","mapY","pixelX","pixelY"])

with open('annolist.json') as f:
    df = json.load(f)
    for resource in df["resources"]:
        print("-----------")
        chars = cleanhtml(resource["resource"][0]["chars"])
        xywh = resource["on"][0]["selector"]["default"]["value"].split("=")[1].split(",")

        x = int(int(xywh[0]) + int(xywh[2]) / 2)
        y = int(xywh[1]) + int(xywh[3])

        x = int(x * r)
        y = int(y * r)

        loc = chars

        for e in arr:
            loc = loc.replace(e["label"], e["value"] + ",")

        spl = loc.split(",")

        lat, lon = float(spl[1]), float(spl[0])

        print(lat, lon)

        loc2 = pyproj.transform(wgs84, jgd2011_9, lat, lon)

        print(chars, loc, xywh, x, y, loc2[0], loc2[1])

        row = [loc2[0], loc2[1], x, -1 * y]
        rows.append(row)

        # break

print(rows)

import csv

with open('gcp.points', 'w') as f:
    writer = csv.writer(f, lineterminator='\n') # 改行コード（\n）を指定しておく
    writer.writerows(rows) # 2次元配列も書き込める