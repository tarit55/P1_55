def binary_search_re(arr,start,end,find):
    if start>end:
        print("value is not present in the array")
        return

    mid=(start+end)//2
 
    if arr[mid]==find:  
            print("value found at index=",mid)
            return
    elif arr[mid] < find:  
            binary_search_re(arr,mid+1,end,find)
    else:  
            binary_search_re(arr,start,mid-1,find)

arr=list(map(int,input("Enter the elements of the array=").split()))
find=int(input("Enter the search element="))
arr.sort()
print("Sorted array=>",arr)
binary_search_re(arr,0,len(arr)-1,find)
