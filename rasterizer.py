import os


class Rasterizer:
    def __init__(self, tempJsonPath, tempRasterPath, tempGeoRefJsonPath, tempGeoRefRasterPath):
        self.tempJsonPath = tempJsonPath
        self.tempRasterPath = tempRasterPath
        self.tempGeoRefJsonPath = tempGeoRefJsonPath
        self.tempGeoRefRasterPath = tempGeoRefRasterPath

    def create_temp_rasters(self):
        for filename in os.listdir(self.tempJsonPath):
            feat_geojson = os.path.join(self.tempJsonPath, filename)
            feat_raster = os.path.join(self.tempRasterPath, filename + ".tif")
            os.system(
                'gdal_rasterize -of gtiff -ot byte -co alpha=yes -burn 255 -burn 0 -burn 0 -burn 100 -ts 100 100 -q ' + feat_geojson + ' ' + feat_raster)

        for filename in os.listdir(self.tempGeoRefJsonPath):
            feat_geojson = os.path.join(self.tempGeoRefJsonPath, filename)
            feat_raster = os.path.join(self.tempGeoRefRasterPath, filename.strip('.geojson') + ".tif")
            os.system(
                'gdal_rasterize -of gtiff -ot byte -co alpha=yes -burn 255 -burn 0 -burn 0 -burn 100 -ts 100 100 -q ' + feat_geojson + ' ' + feat_raster)