import os


jsonfile_path = 'C:/Rasterio_Based_Georeferencing/first_data_source/472639.geojson'
filename = jsonfile_path.strip('.geojson').split('/')[-1]
if not os.path.exists('C:/Rasterio_Based_Georeferencing/shapefiles/' + filename):
    os.makedirs('C:/Rasterio_Based_Georeferencing/shapefiles/' + filename)
shapefile_path = 'C:/Rasterio_Based_Georeferencing/shapefiles/' + filename + '/' + filename +'.shp'
os.system('ogr2ogr -nlt MULTIPOLYGON -skipfailures ' + shapefile_path + ' ' + jsonfile_path)