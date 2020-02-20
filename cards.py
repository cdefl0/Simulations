import random
import sys 

def selectionsort(arr):
    n = len(arr)
    s={"♠":0,"♥":1,"♦":2,"♣":3}
    f={"A":1,"J":11,"Q":12,"K":13}
    
    for i in range(n): 

	low = i 
	for j in range(i+1, n): 
		if A[low] > A[j]: 
			low = j 
	 
	x[i], x[low] = x[low], x[i] 

    print ("Sorted array") 
    for i in range(n): 
	print("%d" %x[i]), 


def shuffle(arr):
    n = len(arr)
    for i in range(n-1,0,-1): 
        j = random.randint(0,i+1) 
        arr[i],arr[j] = arr[j],arr[i]

def deal():
    d=[]
    s=["♠","♥","♦","♣"]
    f={1:"A",11:"J",12:"Q",13:"K"}
    for i in range(4):
        for j in range(1,14):
            d.append(f"{f[j] if j in f else j}{s[i]}")
    return d

###

cards = deal()
print("Before shuffle: ")
print(cards)

shuffle(cards)
print("After shuffle: ")
print(cards)
