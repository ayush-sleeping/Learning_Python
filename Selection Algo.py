# Aim:- Python program for finding the smallest element in an array A of size n using Selection Algorithm.


import sys
print("Enter size of an array ")
s=int(input())
i=0
ar=[]

print("Enter array elements ")
while i<s:
	ar.append(int(input()))
	i=i+1

print("Array values you enteres is: ")
print(ar)

for i in range(len(ar)):                # Traverse through all array elements
	min_idx=i                           # Find the minimum element in remaining unsorted array
	for j in range(i+1, len(ar)):
		if ar[min_idx]>ar[j]:
			min_idx=j

			ar[i], ar[min_idx]=ar[min_idx], ar[i]     # Swap the found minimum element with the first element

print("Sorted array")                # Driver Code to test above code
for i in range(len(ar)):
	print("%d"%ar[i]),
	
print("Smallest Element: %d"%ar[0])
print("Largest Element: %d"%ar[s-1])