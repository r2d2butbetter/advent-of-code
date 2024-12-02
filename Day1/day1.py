import sys
import re

def getinput():
    list1 = []
    list2 = []
    with open('Day1/input.txt', 'r') as file:
        for line in file:
            num1, num2 = map(int, line.split())
            list1.append(num1)
            list2.append(num2)
    return list1, list2


if __name__ =="__main__":
    l1, l2= getinput()[0], getinput()[1]
    l1.sort()
    l2.sort()
    l3 = []
    for i in range(len(l1)):
      l3.append(abs(l2[i] - l1[i]))
    print("Part1: ", sum(l3))

    l4=[]
    for a in l1:
        sc=a*l2.count(a)
        l4.append(sc)
    print("Part2: ",sum(l4))