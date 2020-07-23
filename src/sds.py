import os
class Sds:
    def __init__(self,dire=None,reverse = False):
        self.path  = dire
        self.reverse=reverse
        self.core()


    def getFileSize(self,dire):
        return os.stat(dire).st_size

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

    def core(self):
        path  = self.fixPath(self.path)
        loglist = self.sort(self.calcSizes(self.path),self.reverse)
        self.repr(loglist)


    def repr(self,loglist):
        for dire,size in loglist:
            print(dire ,'   ',self.convertTo(size))


    def fixPath(self,dire):
        return dire.replace('\\','/')

    def buildPath(self,*args):
        return '/'.join(args)

    def calcSizes(self,path):
        path      = path
        loglist   = []
        buildPath = self.buildPath
        for cur in os.listdir(path):
            if os.path.isdir(buildPath(path,cur))  == False:
                continue
            val = 0
            for i in os.walk(buildPath(path,cur)):
                for j in i[2]:
                    trgt = buildPath(i[0],j)
                    if not os.path.isfile(trgt):
                        continue
                    val += self.getFileSize(trgt)
            loglist.append((cur,val))
        return loglist

    def sort(self,loglist,reverse = False):
        loglist.sort(key = lambda ele : ele[1],reverse = reverse)
        return loglist

