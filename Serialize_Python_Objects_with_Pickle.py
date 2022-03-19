####
####
####

import pickle
mytext = "Hello World"
myint = 18
myfloat = 7.657

with open('mydata.txt', 'w') as f:
    f.write(mytext + '\n')
    f.write(str(myint) + '\n')
    f.write(str(myfloat) + '\n')

with open('mydata.txt', 'r') as f:
    data = f.read().splitlines()
    mytext = data[0]
    myint = int(data[1])
    myfloat = float(data[2])

print(mytext, myint, myfloat)

mydict = {'A':18, 'B': 99, 'H': 76}

class Person:
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight
    def print_info(self):
        print(self.name)
        print(self.age)
        print(self.weight)
    def get_older(self,years):
        self.age += years
    
p1 = Person('Mike', 25, 189)
p1.print_info()
p1.get_older(6)
p1.print_info()

with open('mike.pickle', 'wb') as f: #wb = writing bytes mode  #creates binary object.
    pickle.dump(p1, f)
with open('mike.pickle', 'rb') as f:
    p1 = pickle.load(f)
    
p1.print_info()