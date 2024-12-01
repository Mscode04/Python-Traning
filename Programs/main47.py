def words():
    f=open('eword.txt', 'r')
    lines = f.readlines()
    count=0
    for line in lines:
        for word in line.split():
            if word.endswith('e'):
                count+=1
    print("Number of Words ", count)
    f.close()
words()
