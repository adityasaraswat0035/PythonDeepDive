from take import take
from distinct import distinct

def run_pipeline():
    items=[3,6,6,2,1,1]
    for item in take(3,distinct(items)):
        print(item)

run_pipeline()
items=[3,6,6,2,1,1]
x=take(3,distinct(items))
print(type(x))