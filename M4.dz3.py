import colorama
import pathlib 
import sys
colorama.init(autoreset=True)
#for arg in sys.argv if len(sys.argv)<2 else 
    #print(arg[1])
#print(sys.argv[1])
path = sys.argv[1]
p = pathlib.Path(path)
def listdir(path, tab=0):
    p = pathlib.Path(path)
    lst=p.iterdir()
    for el in lst:
        if el.is_dir():
            print(colorama.Fore.GREEN+(tab*" ")+'\\'+el.name)
            listdir(el,tab+1)
        else:
            print(colorama.Fore.LIGHTBLUE_EX+(tab*" ")+'|'+el.name)    
listdir(path=path)        