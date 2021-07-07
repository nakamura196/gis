import pyproj
import csv 

wgs84=pyproj.CRS("EPSG:4326")
jgd2011_9 = pyproj.CRS("EPSG:3857")
lat, lon = 35.71, 139.74
print( pyproj.transform(wgs84, jgd2011_9, lat, lon) )

width = 5921
height = 6466

th = 5000

l = max(width, height)

r = 1
if l > th:
    r = th / l

rows = []
rows.append(["mapX","mapY","pixelX","pixelY","enable","dX","dY","residual"])

with open('data.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

        if row[5] == "":
            continue

        lon = float(row[0])
        lat = float(row[1])

        res = pyproj.transform(wgs84, jgd2011_9, lat, lon)

        lat2 = res[0]
        lon2 = res[1]

        print("aaa", lat2, lon2)

        pixelX = float(row[2]) + float(row[4]) / 2
        pixelY =  -1 * (float(row[3]) + float(row[5]) / 2)

        rows.append([lat2, lon2, pixelX * r, pixelY * r, 1, "", "", ""])



with open('aaa.points', 'w') as f:
    writer = csv.writer(f, lineterminator='\n') # 改行コード（\n）を指定しておく
    writer.writerows(rows) # 2次元配列も書き込める