def binary_search(arr,find):
    start= 0
    end = len(arr) - 1

    while start <= end:
        mid=(start+end)//2  
        if arr[mid]==find:  
            print("value found at index=",mid)
            return
        elif arr[mid] < find:  
            start=mid+1
        else:  
            end=mid-1
        
    print("value is not present in the array")

arr=list(map(int,input("Enter the elements of the array=").split()))
find=int(input("Enter the search element="))
arr.sort()
print("Sorted array=>",arr)
binary_search(arr,find)
