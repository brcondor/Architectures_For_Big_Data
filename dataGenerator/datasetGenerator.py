from dataGenerator import *
from dataGenerator.rowGenerator import *

class datasetGenerator(object):
    def __init__(self, rowType="log"):
        self.rowType = rowType
        self.generators = []

    def addGenerator(self,typeGenerator,keyName=False,**args):
        self.generators.append({"generator":typeGenerator,"keyName":keyName,"args":args})

    def removeGenerator(self,keyName):
        self.generators = [gen for gen in self.generators if gen.get("keyName") != keyName]

    def generateRow(self):
        row = {}
        for gen in self.generators:
            if not gen.get("keyName"):
                gen.get("generator").addDict(row,**gen.get("args"))
            else:
                gen.get("generator").addDict(row,gen.get("keyName"),**gen.get("args"))
        return row

    def generateDataset(self,numRows):
        return [self.generateRow() for k in range(numRows)]

