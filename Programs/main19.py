#Pattern 1

for x in range(6):
    for y in range(x):
        print('*', end='')
    print()
for x in range(5,0,-1):
    for y in range(x):
        print('*', end='')
    print()



#Pattern2
# c=0
# for x in range(6):
#     for y in range(1,x):
#         c = c + 1
#         print(c, end='')
#     print()


#Pattern3
# for x in range(7,0,-1):
#     for y in range(7-x):
#         print(" $", end="")
#     print()
#     for z in range(x,1,-1):
#         print(" ", end='')


# #Pattern4
# for x in range(6,0,-1):
#     for y in range(x,7):
#         print(y, end='')
#     print()