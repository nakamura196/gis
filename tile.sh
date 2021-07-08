gdal_translate -mask 4 trans_modified.tif trans.tif
gdal2tiles.py trans.tif docs/gousei -z3-12 --xyz --processes=1