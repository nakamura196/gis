import shutil
from osgeo import gdal, osr

orig_fn = 'test.tif'
output_fn = 'output.tif'

# Create a copy of the original file and save it as the output filename:
shutil.copy(orig_fn, output_fn)
# Open the output file for writing for writing:
ds = gdal.Open(output_fn, gdal.GA_Update)
# Set spatial reference:
sr = osr.SpatialReference()
sr.ImportFromEPSG(2193) #2193 refers to the NZTM2000, but can use any desired projection

# Enter the GCPs
#   Format: [map x-coordinate(longitude)], [map y-coordinate (latitude)], [elevation],
#   [image column index(x)], [image row index (y)]
gcps = [gdal.GCP(1681255.524654, 6120217.357425, 0, 176.412984, 310.977264),
gdal.GCP(1681158.424227, 6120406.821253, 0, 160.386905, 141.487145),
gdal.GCP(1681556.948690, 6120335.658359, 0, 433.204947, 310.547238)]

# Apply the GCPs to the open output file:
ds.SetGCPs(gcps, sr.ExportToWkt())

# Close the output file in order to be able to work with it in other programs:
ds = None