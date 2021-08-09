class ExampleIterator:
    def __init__(self):
        self.index=0
        self.data=[1,2,3]
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index>=len(self.data):
            raise StopIteration()
        rslt=self.data[self.index]
        self.index+=1
        return rslt



class ExampleIterable:
    def __init__(self):
            self.data=[1,2,3]


    def __iter__(self):
        return ExampleIterable.ExampleIteratorV2(self.data)


    class ExampleIteratorV2:
        def __init__(self,data):
            self.index=0
            self.data=data

        def __next__(self):
            if self.index>=len(self.data):
                raise StopIteration()
            rslt=self.data[self.index]
            self.index+=1
            return rslt
    

class AlternateIterable:
    def __init__(self):
        self.data=[1,2,3]
        

    def __getitem__(self,index):
        return self.data[index]


import datetime
i=iter(datetime.datetime.now,None)
print(next(i))
print(next(i))
print(next(i))
print(next(i))

def main():
    i=ExampleIterator()
    try:
        print(next(i))
        print(next(i))
        print(next(i))
        print(next(i))
    except StopIteration:
        print("No more element")
    for i in ExampleIterator():
        print(i)
    
    for i in ExampleIterable():
        print(i)

    for i in AlternateIterable():
        print(i)

if __name__=="__main__":
    main()