import os
from osgeo import ogr


class FinalDataSource:
    def __init__(self, final_datasource):
        self.final_datasource = final_datasource

    def create_final_datasource(self):
        driver_geoJSON = ogr.GetDriverByName('GeoJSON')
        datasourceJSON = driver_geoJSON.CreateDataSource(self.final_datasource)
        layerJSON = datasourceJSON.CreateLayer("feature")

        for filename in os.listdir('C:/Rasterio_Based_Georeferencing/first_data_source'):
            filePath = os.path.join('C:/Rasterio_Based_Georeferencing/first_data_source/', filename)
            print(filePath)
            temp_ds = driver_geoJSON.Open(filePath)
            if temp_ds is None:
                continue
            layer = temp_ds.GetLayer(0)
            for feat in layer:
                layerJSON.CreateFeature(feat)
