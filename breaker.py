import os
from osgeo import ogr


class Breaker:
    def __init__(self, final_list):
        self.final_list = final_list
        self.driver = ogr.GetDriverByName('GeoJSON')

    def jsonGeneration_georef(self, filepath, target_directory_path, khasra_name):

        # Open geoJSON vector source

        datasource = self.driver.Open(filepath)
        if datasource is None:
            return
        layer = datasource.GetLayer(0)
        i = 0
        for feature in layer:
            i = i + 1
            id_no = feature.GetField("objectid")
            khasranum = feature.GetField(str(khasra_name))
            if khasranum in self.final_list:
                khasra_copy = khasranum
                feat_geojson = target_directory_path + "/" + '_'.join(khasra_copy.split('/')) + ".geojson"

                if os.path.exists(feat_geojson):
                    self.driver.DeleteDataSource(feat_geojson)

                feat_dataSource = self.driver.CreateDataSource(feat_geojson)

                if feat_dataSource is None:
                    continue

                print(feat_dataSource)
                dataSource_layer = feat_dataSource.CreateLayer("feature_" + str(i), geom_type=ogr.wkbPolygon)

                # Add an ID field
                idField = ogr.FieldDefn("id", ogr.OFTString)
                dataSource_layer.CreateField(idField)

                uid = ogr.FieldDefn("UNQID", ogr.OFTString)
                dataSource_layer.CreateField(uid)

                did = ogr.FieldDefn("DISTRICT_ID", ogr.OFTString)
                dataSource_layer.CreateField(did)

                tid = ogr.FieldDefn("TEHSIL_ID", ogr.OFTString)
                dataSource_layer.CreateField(tid)

                rid = ogr.FieldDefn("R_I_ID", ogr.OFTString)
                dataSource_layer.CreateField(rid)

                hid = ogr.FieldDefn("HALKA_ID", ogr.OFTString)
                dataSource_layer.CreateField(hid)

                vid = ogr.FieldDefn("VILLAGE_ID", ogr.OFTString)
                dataSource_layer.CreateField(vid)

                kid = ogr.FieldDefn("KHASRA_ID", ogr.OFTString)
                dataSource_layer.CreateField(kid)

                bcode = ogr.FieldDefn("BHUCODE", ogr.OFTString)
                dataSource_layer.CreateField(bcode)

                kd = ogr.FieldDefn("KID", ogr.OFTString)
                dataSource_layer.CreateField(kd)

                objectid = ogr.FieldDefn("objectid", ogr.OFTString)
                dataSource_layer.CreateField(objectid)

                accode = ogr.FieldDefn("accode", ogr.OFTString)
                dataSource_layer.CreateField(accode)

                districtc = ogr.FieldDefn("districtc", ogr.OFTString)
                dataSource_layer.CreateField(districtc)

                tehsilcode = ogr.FieldDefn("tehsilcode", ogr.OFTString)
                dataSource_layer.CreateField(tehsilcode)

                blockcode = ogr.FieldDefn("blockcode", ogr.OFTString)
                dataSource_layer.CreateField(blockcode)

                gpcode = ogr.FieldDefn("gpcode", ogr.OFTString)
                dataSource_layer.CreateField(gpcode)

                lgdgpcode = ogr.FieldDefn("lgdgpcode", ogr.OFTString)
                dataSource_layer.CreateField(lgdgpcode)

                ccode11 = ogr.FieldDefn("ccode11", ogr.OFTString)
                dataSource_layer.CreateField(ccode11)

                villageh = ogr.FieldDefn("villageh", ogr.OFTString)
                dataSource_layer.CreateField(villageh)

                villagee = ogr.FieldDefn("villagee", ogr.OFTString)
                dataSource_layer.CreateField(villagee)

                ccode91 = ogr.FieldDefn("ccode91", ogr.OFTString)
                dataSource_layer.CreateField(ccode91)

                ccode01 = ogr.FieldDefn("ccode01", ogr.OFTString)
                dataSource_layer.CreateField(ccode01)

                khasranum_new = ogr.FieldDefn("khasranum", ogr.OFTString)
                dataSource_layer.CreateField(khasranum_new)

                UNQID, DISTRICT_ID, TEHSIL_ID, R_I_ID, HALKA_ID, VILLAGE_ID, KHASRA_ID, BHUCODE, KID = None, None, None, None, None, \
                                                                                                       None, None, None, None

                for non_geo_file in os.listdir('C:/Rasterio_Based_Georeferencing/non_georef_breaking'):
                    non_geo_khasra = non_geo_file.strip('.geojson').split('/')[-1]
                    non_geo_file_path = 'C:/Rasterio_Based_Georeferencing/non_georef_breaking/' + non_geo_file
                    if '/'.join(non_geo_khasra.split('_')) == str(khasranum):
                        datasource_non_geo = self.driver.Open(non_geo_file_path)
                        if datasource_non_geo is None:
                            return
                        layer_non_geo = datasource_non_geo.GetLayer(0)

                        for feature_new in layer_non_geo:
                            UNQID = feature_new.GetField('UNQID')
                            DISTRICT_ID = feature_new.GetField('DISTRICT_ID')
                            TEHSIL_ID = feature_new.GetField('TEHSIL_ID')
                            R_I_ID = feature_new.GetField('R_I_ID')
                            HALKA_ID = feature_new.GetField('HALKA_ID')
                            VILLAGE_ID = feature_new.GetField('VILLAGE_ID')
                            KHASRA_ID = feature_new.GetField('KHASRA_ID')
                            BHUCODE = feature_new.GetField('BHUCODE')
                            KID = feature_new.GetField('KID')

                            print(UNQID, DISTRICT_ID, TEHSIL_ID, R_I_ID, HALKA_ID, VILLAGE_ID, KHASRA_ID, BHUCODE, KID)

                geom = feature.GetGeometryRef()
                ccode01 = feature.GetField("ccode01")
                ccode91 = feature.GetField("ccode91")
                villagee = feature.GetField("villagee")
                villageh = feature.GetField("villageh")
                ccode11 = feature.GetField("ccode11")
                lgdgpcode = feature.GetField("lgdgpcode")
                gpcode = feature.GetField("gpcode")
                blockcode = feature.GetField("blockcode")
                tehsilcode = feature.GetField("tehsilcode")
                districtc = feature.GetField("districtc")
                accode = feature.GetField("accode")
                objectid = feature.GetField("objectid")

                featureDefn = dataSource_layer.GetLayerDefn()
                feat = ogr.Feature(featureDefn)

                feat.SetGeometry(geom)
                feat.SetField("id", id_no)
                feat.SetField("objectid", objectid)
                feat.SetField("accode", accode)
                feat.SetField("districtc", districtc)
                feat.SetField("tehsilcode", tehsilcode)
                feat.SetField("blockcode", blockcode)
                feat.SetField("gpcode", gpcode)
                feat.SetField("lgdgpcode", lgdgpcode)
                feat.SetField("ccode11", ccode11)
                feat.SetField("villageh", villageh)
                feat.SetField("villagee", villagee)
                feat.SetField("ccode91", ccode91)
                feat.SetField("ccode01", ccode01)
                feat.SetField("khasranum", str(khasranum))
                feat.SetField('UNQID', UNQID)
                feat.SetField('DISTRICT_ID', DISTRICT_ID)
                feat.SetField('TEHSIL_ID', TEHSIL_ID)
                feat.SetField('R_I_ID', R_I_ID)
                feat.SetField('HALKA_ID', HALKA_ID)
                feat.SetField('VILLAGE_ID', VILLAGE_ID)
                feat.SetField('KHASRA_ID', KHASRA_ID)
                feat.SetField('BHUCODE', BHUCODE)
                feat.SetField('KID', KID)
                dataSource_layer.CreateFeature(feat)

                print(feat_geojson)

                feat = None
                feat_dataSource = None

                # print(feature)
        datasource = None

    def jsonGeneration_non_georef(self, filepath, target_directory_path, khasra_name):

        # Open geoJSON vector source

        datasource = self.driver.Open(filepath)
        if datasource is None:
            return
        layer = datasource.GetLayer(0)
        i = 0
        for feature in layer:
            i = i + 1
            khasranum = feature.GetField(str(khasra_name))
            if khasranum in self.final_list:
                khasra_copy = khasranum
                feat_geojson = target_directory_path + "/" + '_'.join(khasra_copy.split('/')) + ".geojson"

                if os.path.exists(feat_geojson):
                    self.driver.DeleteDataSource(feat_geojson)

                feat_dataSource = self.driver.CreateDataSource(feat_geojson)

                if feat_dataSource is None:
                    continue

                print(feat_dataSource)
                dataSource_layer = feat_dataSource.CreateLayer("feature_" + str(i), geom_type=ogr.wkbPolygon)

                # Add an ID field

                uid = ogr.FieldDefn("UNQID", ogr.OFTString)
                dataSource_layer.CreateField(uid)

                did = ogr.FieldDefn("DISTRICT_ID", ogr.OFTString)
                dataSource_layer.CreateField(did)

                tid = ogr.FieldDefn("TEHSIL_ID", ogr.OFTString)
                dataSource_layer.CreateField(tid)

                rid = ogr.FieldDefn("R_I_ID", ogr.OFTString)
                dataSource_layer.CreateField(rid)

                hid = ogr.FieldDefn("HALKA_ID", ogr.OFTString)
                dataSource_layer.CreateField(hid)

                vid = ogr.FieldDefn("VILLAGE_ID", ogr.OFTString)
                dataSource_layer.CreateField(vid)

                kid = ogr.FieldDefn("KHASRA_ID", ogr.OFTString)
                dataSource_layer.CreateField(kid)

                bcode = ogr.FieldDefn("BHUCODE", ogr.OFTString)
                dataSource_layer.CreateField(bcode)

                kd = ogr.FieldDefn("KID", ogr.OFTString)
                dataSource_layer.CreateField(kd)

                geom = feature.GetGeometryRef()
                KID = feature.GetField("KID")
                BHUCODE = feature.GetField("BHUCODE")
                KHASRA_ID = feature.GetField("KHASRA_ID")
                VILLAGE_ID = feature.GetField("VILLAGE_ID")
                HALKA_ID = feature.GetField("HALKA_ID")
                R_I_ID = feature.GetField("R_I_ID")
                TEHSIL_ID = feature.GetField("TEHSIL_ID")
                DISTRICT_ID = feature.GetField("DISTRICT_ID")
                UNQID = feature.GetField("UNQID")

                featureDefn = dataSource_layer.GetLayerDefn()
                feat = ogr.Feature(featureDefn)

                feat.SetGeometry(geom)
                feat.SetField("UNQID", UNQID)
                feat.SetField("KID", KID)
                feat.SetField("BHUCODE", BHUCODE)
                feat.SetField("KHASRA_ID", KHASRA_ID)
                feat.SetField("VILLAGE_ID", VILLAGE_ID)
                feat.SetField("HALKA_ID", HALKA_ID)
                feat.SetField("R_I_ID", R_I_ID)
                feat.SetField("TEHSIL_ID", TEHSIL_ID)
                feat.SetField("DISTRICT_ID", DISTRICT_ID)
                dataSource_layer.CreateFeature(feat)

                print(feat_geojson)

                feat = None
                feat_dataSource = None

                # print(feature)
        datasource = None