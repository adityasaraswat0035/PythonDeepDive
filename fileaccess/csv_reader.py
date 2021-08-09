import csv
if __name__=="__main__":
    try:
        best_sellers_data=open("best_sellers.csv",mode="rt",encoding="utf-8")
        best_sellers=csv.reader(best_sellers_data)
        for item in best_sellers:
            print(item[0],':',item[1])
    except OSError as ex:
        print(ex)
    finally:
        best_sellers_data.close()