with open("ending_file.txt","rt") as f:
    for line in iter(lambda :f.readline().strip(),"END"):
        print(line)