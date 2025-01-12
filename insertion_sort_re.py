def insertion_sort_re(arr,n):
        if n <=1:
            return
        insertion_sort_re(arr,n-1)
        sorted=arr[n-1]
        j=n-2

        while j>=0 and arr[j]>sorted:
            arr[j+1]=arr[j]
            j=j-1      
        arr[j+1]=sorted

arr=list(map(int,input("Enter the elements of the array=").split()))
print("Original array=>",arr)
insertion_sort_re(arr,len(arr))
print("Sorted array=>",arr)