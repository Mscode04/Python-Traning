def counts():
    # Open the file in read mode
    f=open("story.txt", 'r')
    lines = f.readlines()
    count=0
    for x in lines:
        if x.startswith('T'):
            count+=1
    print("Number of lines ",count)
    f.close()
counts()
