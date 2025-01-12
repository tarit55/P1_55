def insertion_sort(arr):
    for i in range(1,len(arr)):
        sorted=arr[i]
        j=i-1

        while j>=0 and arr[j]>sorted:
            arr[j+1]=arr[j]
            j=j-1      
        arr[j+1]=sorted

arr=list(map(int,input("Enter the elements of the array=").split()))
print("Original array=>",arr)
insertion_sort(arr)
print("Sorted array=>",arr)