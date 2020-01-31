import re


class ListGenerator:
    def __init__(self, driver, previous_geo_ref_jsonFile, intermediate_geo_ref_json_file):
        self.tempDict = {}
        self.kidList = []
        self.khasraNumList = []
        self.finalList = []
        self.remainingList = []
        self.remainingGeoRefList = []
        self.driver = driver
        self.previous_geo_ref_jsonFile = previous_geo_ref_jsonFile
        self.intermediate_geo_ref_json_file = intermediate_geo_ref_json_file

    def createLists(self):
        datasource1 = self.driver.Open(self.previous_geo_ref_jsonFile)
        layer1 = datasource1.GetLayer(0)
        for feature in layer1:
            khasranum = feature.GetField("khasranum")
            self.khasraNumList.append(khasranum)

        #print(self.khasraNumList)

        datasource2 = self.driver.Open(self.intermediate_geo_ref_json_file)
        layer2 = datasource2.GetLayer(0)
        for feat2 in layer2:
            KID = feat2.GetField("KID")
            self.kidList.append(KID)
        #print(kid_extras)

        #print(self.kidList)

        for i in self.khasraNumList:
            if i in self.kidList:
                self.finalList.append(i)
        print(self.finalList)

        for j in self.kidList:
            if j not in self.khasraNumList:
                self.remainingList.append(j)
        print(self.remainingList, len(self.remainingList))

        for k in self.khasraNumList:
            if k not in self.finalList:
                self.remainingGeoRefList.append(k)
        print(self.remainingGeoRefList, len(self.remainingGeoRefList))

    def create_Dictionary_For_Remaining_Khasras(self):
        list = []
        # y = 0
        for i in self.remainingGeoRefList:
            if i is None:
                continue
            # if '/' in i:
                # y = len(i.split('/'))
            for j in self.remainingList:
                if j is None:
                    continue
                # print(i, " ", j)
                # if j is None or len(i.split('/')) > len(j.split('/')):
                #    continue
                # if y > 0:
                #    x = [j.split('/')[r]for r in range(y) if y > 2]
                # else:
                x = j.split('/')[0]
                if str(i) == str(x):
                    list.append(j)
            # print(list)
            copy = list.copy()
            self.tempDict[i] = copy
            list.clear()
            # print(self.tempDict)
        return self.tempDict, self.finalList, self.remainingGeoRefList, self.remainingList