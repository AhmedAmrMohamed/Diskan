from . import DSG
from . import Node
from . import Printer
from . import MSG
import os
import time

DSG = DSG.DSG
Node= Node.Node
Printer = Printer.Printer
def verify(path):
    x = os.path
    return not x.islink(path) and x.isdir(path)

def getworkingdir():
    workingdir = os.getcwd()
    print(MSG.usethisdir)
    print(workingdir)
    choice = getchoice()
    if choice == 'y': return workingdir
    while True:
        workingdir = input(MSG.entertrgt)
        if workingdir.startswith('~'):
            workingdir = os.path.expanduser(workingdir)
        if verify(workingdir):
            return workingdir
        print(MSG.invaliddir)

def getnode(workingdir):
    t0 = time.time()
    try:
        dsg = DSG(workingdir)
        print(dsg.rootnode.getsize())
    except PermissionError:
        print(MSG.permdenied)
        exit()
    print(MSG.proccessedin, time.time()-t0,'s')
    return dsg.rootnode

def getchoice(dispmsg = None) : 
    if not dispmsg:
        dispmsg = ""
    return input(dispmsg).strip().lower()

def exit():
    print(MSG.bye)
    quit()

def main():
    try:
        workingdir = getworkingdir()
        rootnode = getnode(workingdir)
        printer = Printer(True, rootnode)
        printer.print()
        choice = ""
        while (choice:= getchoice(MSG.entercommand)) != 'e':
            if choice == 'h':
                print(MSG.allcommands)
                continue
            try:
                expval, dirnum = choice.split()
                if expval in 'fe':
                    expval = True if expval == 'e' else False
                    dirnum = int(dirnum)
                    printer.setexpand(dirnum,expval)
                    printer.print()
                else:
                    raise ValueError
            except ValueError:
                print('wrong command format')
    except KeyboardInterrupt:
        exit()
    exit()

    
