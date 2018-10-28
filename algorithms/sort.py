
"""
progress the highest value to the right: O(N2)
"""
def bubbleSort(a):
    print("bubbleSort")
    for i in range(len(a)-1,1,-1):
        print(a)
        for j in range(0,i):
            if a[j] > a[j+1]:
                s=a[j]
                a[j]=a[j+1]
                a[j+1]=s
    return a

"""
select the lowest among the serie and place it on the left :
# of comparisons is  n*(n-1)/2  O(N2)
"""
def selectionSort(a):
    print("selectionSort")
    for i in range(0,len(a)):
        min=i
        for j in range(i+1,len(a)):
            if a[j] < a[min]:
                min=j
        s=a[i]
        a[i]=a[min]
        a[min]=s
        print(a)
    return a

"""
from a given i (market element), the array on left side of i is partially sorted, the algo adds element at i to the correct position in the left side - O(N2)
"""
def insertionSort(a):
    print("Insertion Sort")

    for i in range(1,len(a)):
        v=a[i]
        j=i
        print(a)
        while j > 0 and a[j-1] >= v:
            a[j]=a[j-1]  # shift to the right
            j-=1
        a[j]=v
    return a

def swap(a,i,j):
    s=a[i]
    a[i]=a[j]
    a[j]=s

"""
The algo has two phases: partition the collection and sort the partitions.
To partition the collection select the pivot where each element on left side of the pivot are smaller than the pivot and any element on right side of the pivot are higher.
"""
def quickSort(a):
    print("quickSort")
    qssort(a,0,len(a)-1)
    return a

def qspartition(a,low,high):
    p=a[high]
    i=low  # used to search for higher value than the jth one
    for j in range(low,high):
        if a[j] < p :
            if i != j:
                swap(a,i,j)
            i += 1
    swap(a,i,high)
    return i

def qssort(a,low,high):
    print(a,low,high)
    if low < high:
        pivot = qspartition(a,low,high)
        qssort(a,low,pivot-1)
        qssort(a,pivot+1,high)

b=bubbleSort([1,2,5,12,3,9,10,8])
print(b)
b=selectionSort([1,2,5,12,3,9,10,8])
print(b)

print(insertionSort([1,2,5,12,3,9,10,8]))

print(quickSort([1,2,5,12,3,9,10,8]))
