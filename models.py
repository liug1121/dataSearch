from django.db import models

class Datas:
    ID_A0M05 = 'A0M05'
    NAME_A0M05 = '各级各类学校数'
    dataType = -1
    dataName = ''
    datas = {}

    def __init__(self, dataType, dataName):
        self.dataType = dataType
        self.dataName = dataName

    def setDatas(self, datas):
        self.datas = datas

class Index:
    id = -1
    name = ''

    def __init__(self, id, name):
        self.id = id
        self.name = name



