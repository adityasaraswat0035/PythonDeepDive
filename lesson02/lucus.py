def lucus():
    yield 2
    a=2
    b=1
    while True:
        yield b
        a,b=b,a+b

if __name__=="__main__":
    for numb in lucus():
        print(numb,"\n")