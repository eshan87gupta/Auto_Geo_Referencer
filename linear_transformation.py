from osgeo import gdal, ogr, osr


class LinearTransformation:
    def __init__(self, rem_geo_ref_raster_file_path, rem_non_geo_ref_raster_file_path):
        self.longList = []
        self.latList = []
        self.non_ref_longList = []
        self.non_ref_latList = []
        self.lonDict = {}
        self.latDict = {}

        self.rem_geo_ref_raster_file_path = rem_geo_ref_raster_file_path
        self.rem_non_geo_ref_raster_file_path = rem_non_geo_ref_raster_file_path

    def getExtent(self, gt, cols, rows):
        ext = []
        xarr = [0, cols]
        yarr = [0, rows]

        for px in xarr:
            for py in yarr:
                x = gt[0] + (px * gt[1]) + (py * gt[2])
                y = gt[3] + (px * gt[4]) + (py * gt[5])
                ext.append([x, y])
                print(x, y)
            yarr.reverse()
        return ext

    def create_dict_for_first_raster_matching(self):
        ds = gdal.Open(self.rem_non_geo_ref_raster_file_path)
        if ds is None:
            return
        gt = ds.GetGeoTransform()
        print(gt)
        cols = ds.RasterXSize
        rows = ds.RasterYSize
        print(1)
        print(cols, rows)
        ext = self.getExtent(gt, cols, rows)
        print(2)
        print(ext)

        long = ext[0][0]
        lat = ext[0][1]
        self.non_ref_longList.append(long)
        self.non_ref_latList.append(lat)
        for i in range(cols):
            long = long + gt[1]
            self.non_ref_longList.append(long)
            lat = lat + (gt[5])
            self.non_ref_latList.append(lat)

    def create_dict_for_second_raster_matching(self):
        ds = gdal.Open(self.rem_geo_ref_raster_file_path)
        if ds is None:
            return
        gt = ds.GetGeoTransform()
        print(gt)
        cols = ds.RasterXSize
        rows = ds.RasterYSize
        print(1)
        print(cols, rows)
        ext = self.getExtent(gt, cols, rows)
        print(2)
        print(ext)

        long = ext[0][0]
        lat = ext[0][1]
        self.longList.append(long)
        self.latList.append(lat)
        for i in range(cols):
            long = long + gt[1]
            self.longList.append(long)
            lat = lat + (gt[5])
            self.latList.append(lat)

    def generateGeoReferencedGeoJSON(self, pathNonGeoRef, georefpath):
        id_val = None
        print('hi')
        print(georefpath)
        driver = ogr.GetDriverByName("geojson")
        spatialReference = osr.SpatialReference()
        spatialReference.SetWellKnownGeogCS("WGS84")
        dataSource = driver.CreateDataSource(georefpath)

        dataSource_layer = dataSource.CreateLayer("feature", spatialReference)

        id = ogr.FieldDefn("id", ogr.OFTString)
        dataSource_layer.CreateField(id)

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

        khasranum = ogr.FieldDefn("khasranum", ogr.OFTString)
        dataSource_layer.CreateField(khasranum)

        featureDefn = dataSource_layer.GetLayerDefn()
        feat = ogr.Feature(featureDefn)

        driver = ogr.GetDriverByName("geojson")
        datasource = driver.Open(pathNonGeoRef)
        layer = datasource.GetLayer(0)
        print(layer.GetFeatureCount())

        for feature in layer:
            id_val = feature.GetField("id")
            UNQID = feature.GetField("UNQID")
            DISTRICT_ID = feature.GetField("DISTRICT_ID")
            TEHSIL_ID = feature.GetField("TEHSIL_ID")
            R_I_ID = feature.GetField("R_I_ID")
            HALKA_ID = feature.GetField("HALKA_ID")
            VILLAGE_ID = feature.GetField("VILLAGE_ID")
            KHASRA_ID = feature.GetField("KHASRA_ID")
            BHUCODE = feature.GetField("BHUCODE")
            KID = feature.GetField("KID")

            geom = feature.GetGeometryRef()
            poly = ogr.Geometry(ogr.wkbMultiPolygon)
            poly1 = ogr.Geometry(ogr.wkbPolygon)

            for i in geom:
                print(i, "#####################################")
                print(i.GetPointCount())
                ring = ogr.Geometry(ogr.wkbLinearRing)
                for l in range(i.GetPointCount()):
                    point = i.GetPoint(l)
                    print(point)

                    error = []
                    for k in range(len(self.non_ref_longList)):
                        error.append(abs(self.non_ref_longList[k] - point[0]))
                    index = error.index(min(error))
                    x = self.lonDict[self.non_ref_longList[index]]

                    error.clear()
                    for l in range(len(self.non_ref_latList)):
                        error.append(abs(self.non_ref_latList[l] - point[1]))
                    index = error.index(min(error))
                    y = self.latDict[self.non_ref_latList[index]]

                    print("new x ", x, " new y ", y)
                    ring.AddPoint(x, y, 0.0)
                poly1.AddGeometry(ring)
            poly.AddGeometry(poly1)
            feat.SetField("id", id_val)
            feat.SetField("UNQID", UNQID)
            feat.SetField("DISTRICT_ID", DISTRICT_ID)
            feat.SetField("TEHSIL_ID", TEHSIL_ID)
            feat.SetField("R_I_ID", R_I_ID)
            feat.SetField("HALKA_ID", HALKA_ID)
            feat.SetField("VILLAGE_ID", VILLAGE_ID)
            feat.SetField("KHASRA_ID", KHASRA_ID)
            feat.SetField("BHUCODE", BHUCODE)
            feat.SetField("KID", KID)
            feat.SetGeometry(poly)
            dataSource_layer.CreateFeature(feat)

    def create_final_jsons(self, georefpath, file_name):
        for m in range(len(self.non_ref_longList)):
            self.lonDict[self.non_ref_longList[m]] = self.longList[m]

        for n in range(len(self.non_ref_latList)):
            self.latDict[self.non_ref_latList[n]] = self.latList[n]

        self.generateGeoReferencedGeoJSON(georefpath, 'C:/Rasterio_Based_Georeferencing/first_data_source/' + file_name)