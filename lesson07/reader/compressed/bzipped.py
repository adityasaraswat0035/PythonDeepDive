import bz2
import sys 

opener=bz2.open
if __name__=='__main__':
    f=opener(sys.argv[1],mode="wt",encoding="utf-8")
    f.write(" ".join(sys.argv[2]))
    f.close()