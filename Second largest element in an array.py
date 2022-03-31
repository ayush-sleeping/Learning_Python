# Practical no. : 7 -> write python program for finding the second largest element in an array A of the n using Tournament
print("Enter size of an array")
s = int(input())
i = 0
b = []

print("Enter array Elements")
while i < s:
    b.append(int(input()))
    i = i + 1
print(b)

def getSecondHighest(b):
    hi = mid = lo = 0
    for i in range(0, len(b)):
        x = b[i]

        if(x > hi):
            lo = mid
            mid = hi
            hi = x
        elif(x < hi and x > mid):
            lo = mid
            mid = x
        elif(x < lo):
            lo = x
    return mid
print("second highest Element in given array = ", getSecondHighest(b))