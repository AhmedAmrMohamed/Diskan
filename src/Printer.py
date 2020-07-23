# from DSG import DSG
# from Node import Node
# from os import sep
from . import DSG
from . import Node
from os import sep
DSG = DSG.DSG
Node= Node.Node
revsortfunc = lambda x : -x.getsize()
class Printer:
    def __init__(self,besorted, rootnode):
        self.expanded_nodes = {}
        self.sorted   = besorted
        self.rootnode = rootnode
    
    def convertTo(self,size):
        units = ['B','KB','MB','GB','TB']
        ret   = ''
        for lvl in range(4):
            if size >= 1024:
                size/=1024
            else:
                tmp  = int(size*100)%100
                ret  = f'{str(int(size))}.{str(tmp)}{units[lvl]}'
                break
        return ret
    
    def print(self):
        self.__print(self.rootnode,0)

    def __print(self,node, margin ):
        CT  = self.convertTo
        mainpad = ' '*margin+'|--'
        subpad  = ' '*(margin+2)+'|--'
        rjustn  = lambda num  : str(num).rjust(5)
        getname = lambda name : name.split(sep)[-1]
        print(mainpad,
                node.idx,
                getname(node.url),
                CT(node.getsize())
                )

        if self.expanded(node):
            subfiles = node.subfiles
            subnodes = node.subnodes
            if self.sorted:
                subfiles = list(subfiles)
                subfiles.sort(key = lambda x: -x[1])
                subnodes.sort(key = revsortfunc)

            for subfile in subfiles:
                print(subpad,
                        getname(subfile[0]),
                        CT(subfile[1])
                        )
            for subnode in subnodes:
                self.__print(subnode, margin+2)

    def expanded(self, node):
        return self.expanded_nodes.get(node.idx,False)
    
    def setexpand(self,nodeidx,expand):
        self.expanded_nodes[nodeidx] = expand
        
        

