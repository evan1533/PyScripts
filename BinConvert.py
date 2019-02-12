import random

num = input("Enter the number to be converted:\n");

binar = "";
for i in range(0,random.randint(3,11)):
    binar = binar+str(random.randint(0,1))

print(binar)
