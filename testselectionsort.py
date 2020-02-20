import sys 
x = [64, 25, 12, 22, 11] 

for i in range(len(x)): 

	low = i 
	for j in range(i+1, len(x)): 
		if A[low] > A[j]: 
			low = j 
	 
	x[i], x[low] = x[low], x[i] 

print ("Sorted array") 
for i in range(len(x)): 
	print("%d" %x[i]), 
