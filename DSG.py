import os
from Node import Node 

pathjoin = os.path.join
listdir  = os.listdir
isfile   = os.path.isfile
isdir    = os.path.isdir
islink   = os.path.islink

class DSG:
    def __init__(self,rooturl):
        self.rooturl = rooturl
        self.idx=0
        self.rootnode= self.dsg(rooturl)

    
    def dsg(self, url):
        node = Node(url,self.idx)
        self.idx+=1
        size = 0
        for diritr in listdir(url):
            subfile = pathjoin(url,diritr)
            if islink(subfile):
                continue
            if isfile(subfile):
                node.addfile(subfile)
            elif isdir(subfile):
                subnode = self.dsg(subfile)
                node.addsubdir(subnode)
        return node




