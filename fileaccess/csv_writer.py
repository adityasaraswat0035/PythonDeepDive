import csv
from os import read
def read_file():
    try:
        best_sellers_data=open("best_sellers.csv",mode="rt",encoding="utf-8")
        best_sellers=csv.reader(best_sellers_data)
        for item in best_sellers:
            yield item
    except OSError as ex:
        print(ex)
    finally:
        best_sellers_data.close()

if __name__=="__main__":
    best_seller_new=open("best_sellers_new.csv",mode="wt",encoding="utf-8",newline="")
    best_seller_writer=csv.writer(best_seller_new)
    for line in read_file():
        best_seller_writer.writerow(line)