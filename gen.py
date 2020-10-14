import random

firstnames = open("FirstNames.txt",'r').readlines()
lastnames = open("LastNames.txt",'r').readlines()

samples=int(input("enter no of samples:"))

for i in range(1,samples):
    fid =  random.randint(1, len(firstnames)-1)
    lid =  random.randint(1, len(lastnames)-1)
    firstname = firstnames[fid].strip() 
    lastname = lastnames[lid].strip()
    FullName = firstname + " " + lastname
    print(FullName)