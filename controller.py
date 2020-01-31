import os
import shutil
from osgeo import gdal, ogr, osr
from breaker import Breaker
from rasterizer import Rasterizer
from list_generator import ListGenerator
from final_result_generator import FinalDataSource
from linear_transformation import LinearTransformation


def create_final_datasource(path):
    driver_geoJSON = ogr.GetDriverByName('GeoJSON')
    datasourceJSON = driver_geoJSON.CreateDataSource(path)
    layerJSON = datasourceJSON.CreateLayer("feature")

    for filename in os.listdir('C:/Rasterio_Based_Georeferencing/georef_breaking'):
        filePath = 'C:/Rasterio_Based_Georeferencing/georef_breaking' + '/' + filename
        print(filePath)
        temp_ds = driver_geoJSON.Open(filePath)
        if temp_ds is None:
            continue
        layer = temp_ds.GetLayer(0)
        for feat in layer:
            layerJSON.CreateFeature(feat)


def create_DiataSource_Of_Remaining_Khasras(k):
    print(k)
    list = tempDict[k]
    if len(list) > 0:
        ds = driver.CreateDataSource(rem_non_geo_ref_khsra_json_path + k)
        if ds is None:
            return
        else:
            layer = ds.CreateLayer("feature")
            datasource_temp = driver.Open(non_georef_json_path)
            layertemp = datasource_temp.GetLayer(0)
            for feat4 in layertemp:
                KID = feat4.GetField("KID")
                for i in list:
                    if KID == i:
                        layer.CreateFeature(feat4)

        ds_key = driver.CreateDataSource(rem_geo_ref_khasra_json + k)
        if ds_key is None:
            return
        else:
            layer_new = ds_key.CreateLayer("feature")
            datasource_geo_temp = driver.Open(georef_json_path)
            layertemp_geo = datasource_geo_temp.GetLayer(0)
            for feat4_geo in layertemp_geo:
                khasranum = feat4_geo.GetField("khasranum")
                if khasranum == k:
                    layer_new.CreateFeature(feat4_geo)


def ultimate_result_generator(georef_json_path, non_georef_json_path, final_path):
    driver = ogr.GetDriverByName('GeoJSON')
    khasraNumList, kidList, thirdList, finalList, final_out_of_thirdlist, rem_khasra_num_list = [], [], [], [], [], []
    datasource1 = driver.Open(georef_json_path)
    layer1 = datasource1.GetLayer(0)
    for feature in layer1:
        khasranum = feature.GetField("khasranum")
        khasraNumList.append(khasranum)

    datasource2 = driver.Open(non_georef_json_path)
    layer2 = datasource2.GetLayer(0)
    for feat2 in layer2:
        KID = feat2.GetField("KID")
        kidList.append(KID)

    datasource3 = driver.Open(final_path)
    layer3 = datasource3.GetLayer(0)
    for feat3 in layer3:
        KID = feat3.GetField("KID")
        thirdList.append(KID)

    for i in khasraNumList:
        if i in kidList:
            finalList.append(i)
    # print(finalList)

    for j in thirdList:
        if j not in finalList:
            final_out_of_thirdlist.append(j)

    for item in final_out_of_thirdlist:
        new_item = '/'.join(str(item).split('/')[:-1])
        rem_khasra_num_list.append(new_item)

    for new_item in rem_khasra_num_list:
        if new_item in khasraNumList:
            khasraNumList.remove(new_item)

    for final_item in finalList:
        if final_item in khasraNumList:
            khasraNumList.remove(final_item)

    print(khasraNumList)
    copy = georef_json_path
    file_name = copy.split('/')[-1]
    ultimate_ds = driver.CreateDataSource('C:/Rasterio_Based_Georeferencing/ultimate_result/' + file_name)
    ultimate_layer = ultimate_ds.CreateLayer("feature_", geom_type=ogr.wkbMultiPolygon)

    ds_final = driver.Open(final_path)
    layer_final = ds_final.GetLayer(0)
    for feature_final in layer_final:
        ultimate_layer.CreateFeature(feature_final)

    ds = driver.Open(georef_json_path)
    layer = ds.GetLayer(0)
    for feature in layer:
        khasra = feature.GetField('khasranum')
        if khasra in khasraNumList:
            print('hallla booool')
            ultimate_layer.CreateFeature(feature)


def delete_from(directory):
    for the_file in os.listdir(directory):
        file_path = os.path.join(directory, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


if __name__ == '__main__':

    directory_paths = ['C:/Rasterio_Based_Georeferencing/final_result/', 'C:/Rasterio_Based_Georeferencing/first_data_source/',
                       'C:/Rasterio_Based_Georeferencing/georef_breaking/', 'C:/Rasterio_Based_Georeferencing/non_georef_breaking/',
                       'C:/Rasterio_Based_Georeferencing/rem_geo_ref_khasra_raster/', 'C:/Rasterio_Based_Georeferencing/rem_geo_ref_khsra_json',
                       'C:/Rasterio_Based_Georeferencing/rem_non_geo_ref_khasra_raster/', 'C:/Rasterio_Based_Georeferencing/rem_non_geo_ref_khsra_json/']

    for filename in os.listdir("C:/Rasterio_Based_Georeferencing/georef"):
        print(filename)

        for filename2 in os.listdir("C:/Rasterio_Based_Georeferencing/nongeoref"):
            if filename != filename2:
                print(" next file")
                continue

            for path in directory_paths:
                delete_from(path)
            print(filename2)

            georef_json_path = 'C:/Rasterio_Based_Georeferencing/georef/' + filename
            georef_json_path_copy = georef_json_path
            non_georef_json_path = 'C:/Rasterio_Based_Georeferencing/nongeoref/' + filename2
            final_path = 'C:/Rasterio_Based_Georeferencing/final_result/' + georef_json_path_copy.split('/')[-1]

            rem_geo_ref_khasra_json = 'C:/Rasterio_Based_Georeferencing/rem_geo_ref_khsra_json/'
            rem_non_geo_ref_khsra_json_path = 'C:/Rasterio_Based_Georeferencing/rem_non_geo_ref_khsra_json/'

            rem_geo_ref_khasra_raster = 'C:/Rasterio_Based_Georeferencing/rem_geo_ref_khasra_raster'
            rem_non_geo_ref_khsra_raster = 'C:/Rasterio_Based_Georeferencing/rem_non_geo_ref_khasra_raster'

            driver = ogr.GetDriverByName('GeoJSON')

            list_generator = ListGenerator(driver, georef_json_path, non_georef_json_path)
            list_generator.createLists()

            tempDict, finalList, remainingGeoRefList, remainingList = \
                list_generator.create_Dictionary_For_Remaining_Khasras()

            breaker = Breaker(finalList)
            breaker.jsonGeneration_non_georef(non_georef_json_path, 'C:/Rasterio_Based_Georeferencing/non_georef_breaking',
                                              'KID')
            breaker.jsonGeneration_georef(georef_json_path, 'C:/Rasterio_Based_Georeferencing/georef_breaking', 'khasranum')

            first_file_path = 'C:/Rasterio_Based_Georeferencing/first_data_source/' + georef_json_path_copy.split('/')[-1]

            create_final_datasource(first_file_path)

            rem_temp_dict_keys = []
            print(tempDict, len(tempDict))
            for k in tempDict.keys():
                list_keys = tempDict[k]
                if len(list_keys) == 0:
                    rem_temp_dict_keys.append(k)
                create_DiataSource_Of_Remaining_Khasras(k)

            rasterize = Rasterizer(rem_non_geo_ref_khsra_json_path, rem_non_geo_ref_khsra_raster, rem_geo_ref_khasra_json, rem_geo_ref_khasra_raster)
            rasterize.create_temp_rasters()

            for file1 in os.listdir(rem_non_geo_ref_khsra_raster):
                non_ref_longList, non_ref_latList, longList, latList = [], [], [], []
                for file2 in os.listdir(rem_geo_ref_khasra_raster):
                    if file1 == file2:
                        linear_transformer = LinearTransformation('C:/Rasterio_Based_Georeferencing/rem_geo_ref_khasra_raster/' + file2,
                                                                  'C:/Rasterio_Based_Georeferencing/rem_non_geo_ref_khasra_raster/' + file1)
                        linear_transformer.create_dict_for_first_raster_matching()
                        linear_transformer.create_dict_for_second_raster_matching()
                        linear_transformer.create_final_jsons('C:/Rasterio_Based_Georeferencing/rem_non_geo_ref_khsra_json/' +
                                                              file1.strip('.tiff'), file1.strip('.tiff'))

            datasource = FinalDataSource(final_path)
            datasource.create_final_datasource()

            ultimate_result_generator(georef_json_path, non_georef_json_path, final_path)