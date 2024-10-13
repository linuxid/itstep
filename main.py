from random import *
a=[[randint(0,9) for _ in range(10)] for _ in range(10)]
print("Hello world!")
for i in a:
    for j in i:
        print(j,end="\t")
    print()
