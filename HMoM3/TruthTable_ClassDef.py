from itertools import product

class TruthTable():
    i=0
    def __init__(self,argNum,result__list=[]):
        self.argNum=argNum
        self.result__list=result__list
        #self.columnLen=2**argNum
        self.matrix=[]
    
    def makeTruthTable_manual(self):
            
        for i in product((True,False),repeat=self.argNum):
            print(i)
            print('Insert the boolean value')
            i=list(i)
            result=input()
            result=bool(result)
            i.append(result)
            self.matrix.append(i)
            print(self.matrix)
            i=tuple(i)
    
    def makeTruthTable_auto(self):
        if len(self.result__list)!=2**self.argNum:
            print('ERROR in makeTruthTable_auto: lenght of result__list is wrong')
        else:
            for i in product((True,False),repeat=self.argNum):
                print(i)
                print('Insert the boolean value')
                i=list(i)
                result=self.result__list[len(self.matrix)]
                if result in ('True','true','T'):
                    result=True
                elif result in ('False','false','F'):
                    result=False
                i.append(result)
                self.matrix.append(i)
                print(self.matrix)
                i=tuple(i)
            
lista=['False',False,True,True]    
tr=TruthTable(2,lista)
tr.makeTruthTable_auto()
#tr.makeTruthTable_manual()
