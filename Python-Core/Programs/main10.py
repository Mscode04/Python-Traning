data=[("Alice", 25), ("Bob", 30), ("Charlie", 35), ("Diana", 40)]
TotalAge=sum(person[1] for person in data)
print('Average age of this group is : ',(TotalAge)/(len(data)))