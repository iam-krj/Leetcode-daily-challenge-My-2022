class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.list = []
        self.indexCount = -1
        self.listFlatter(nestedList)
    
    def listFlatter(self, elementList):
        for element in elementList:
            if element.getInteger()!=None:
                self.list.append(element.getInteger())
            else:
                self.listFlatter(element.getList())
            
    def next(self) -> int:
        self.indexCount+=1
        return self.list[self.indexCount]
        
    def hasNext(self) -> bool:
        if (self.indexCount+1)<len(self.list):
            return True
        else:
            return False