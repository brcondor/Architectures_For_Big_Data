from dataGenerator import *
from random import randint

class typeGenerator(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def generateEl(self,**args):
        pass

    def addDict(self,d,keyName,**args):
        d[keyName] = self.generateEl(**args)
        return d

class intGenerator(typeGenerator):
    def __init__(self):
        return super().__init__()

    def generateEl(self,*argList,**args):
        if argList:
            args = argList[0]
        min = args.get("min",0)
        max = args.get("max",1000)
        return randint(min, max)

class idGenerator(typeGenerator):
    def __init__(self):
        return super().__init__()

    def generateEl(self,*argList,**args):
        if argList:
            args = argList[0]
        prefix = args.get("prefix","id")
        min = args.get("min",0)
        max = args.get("max",1000)
        return prefix+"_"+str(randint(min, max)).zfill(len(str(max))+1)

    def addDict(self, d,keyName="id", **args):
        return super().addDict(d, keyName,**args)

class dateGenerator(typeGenerator):
    def __init__(self):
        return super().__init__()

    def generateEl(self,*argList,**args):
        if argList:
            args = argList[0]
        startDate = args.get("startDate",datetime(2010,1,1))
        endDate = args.get("endDate",datetime.now())
        minPaceSeconds = args.get("minPaceSeconds",3600)
        maxPaceSeconds = args.get("maxPaceSeconds",datetime.now())
        maxS = int((endDate-startDate).total_seconds())
        return startDate+timedelta(0,randint(minPaceSeconds,maxS))

    def addDict(self, d, keyName="ts", **args):
        return super().addDict(d, keyName,**args)

class tickGenerator(typeGenerator):
    def __init__(self):
        self.lastTick = False
        return super().__init__()

    def generateEl(self,*argList,**args):
        if argList:
            args = argList[0]
        if not self.lastTick:
            self.lastTick = args.get("firstTick",datetime(2010,1,1))
        minTick = args.get("minTick",1)
        maxTick = args.get("maxTick",10)
        self.lastTick += timedelta(0,randint(1,maxTick))
        return self.lastTick