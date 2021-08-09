is_odd=lambda numb:True if numb%2!=0 else False
if __name__=="__main__":
    f=filter(is_odd,[1,2,3,4,5])
    print(f)
    print(list(f))
    positives = filter(lambda x: x > 0, [1, -5, 0, 6, -2, 8])
    print(list(positives))
    trues=filter(None,[0,1,False,True,[],[1,2,3],'','Hello'])
