import os
class Node:
    def __init__(self, url,idx):
        self.idx = idx
        self.url = url
        self.subfiles = []
        self.subnodes  = []
        self.size = 0
        self.subfilesSize = 0
    
    def addfile(self,fileurl):
        assert fileurl.__class__ is str\
                , f"fileurl <{fileurl}> not String"
    
        size = os.path.getsize(fileurl)
        self.subfiles.append((fileurl, size))
        self.size += size
        self.subfilesSize += size

    def addsubdir(self,node):
        assert node.__class__ is Node\
                , f"param not Node, {node.__class__}"  
        assert node not in self.subnodes\
                , f"subdir <{node.url}> already exists\
                in <self.url>"
        
        self.subnodes.append(node)
        self.size+=node.getsize()

    def getsize(self):
        return self.size
    
    def getFilesPercentage(self):
        ret = []
        for fi in self.subfiles:
            ret.append(fi[1]/ self.subfilesSize * 100)
        return ret

    def getDirsPercentage(self):
        ret = [self.subfilesSize/self.size * 100]
        for subnode in self.subnodes:
            ret.append(subnode.size/self.size * 100)
        return ret



   
