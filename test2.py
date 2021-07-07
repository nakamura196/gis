import pyproj
import csv 

wgs84=pyproj.CRS("EPSG:4326")
jgd2011_9 = pyproj.CRS("EPSG:3857")
lat, lon = 40, 128.4
print( pyproj.transform(wgs84, jgd2011_9, lat, lon) )