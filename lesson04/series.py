"""Read and print an integer series."""
import sys
from pprint import pprint as pp

def read_series(filename):
    try:
        f=open(filename,mode= "rt",encoding="utf-8")
        return [int(line.strip()) for line in f]
    finally:
        f.close()
    

def read_seriesV2(filename):
    with open(filename,mode= "rt",encoding="utf-8") as f:
        return [int(line.strip()) for line in f]
        

def main(filename):
    series=read_seriesV2(filename)
    pp(series)


if __name__=="__main__":
    main(sys.argv[1])