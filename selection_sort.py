def selection_sort(arr):
    n = len(arr)
    for j in range(n):
        min_index = j
        for i in range(j+1,n):
            if arr[i]<arr[min_index]:
               min_index = i
        arr[j],arr[min_index] =arr[min_index],arr[j]
arr=list(map(int,input("Enter the elements of the array=").split()))
print("Original array=>",arr)
selection_sort(arr)
print("Sorted array=>", arr)