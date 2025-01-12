def bubble_sort(arr):
    n = len(arr)
    for j in range(n-1):
        for i in range(n-j -1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]

arr=list(map(int,input("Enter the elements of the array=").split()))
print("Original array=>",arr)
bubble_sort(arr)
print("Sorted array=>",arr)