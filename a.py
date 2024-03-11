arr=[1,4,6,7]
arr1=[11,2]
arr+=arr1
i=0
j=len(arr)-1
while(i<=j):
  if arr[i]>arr[j]:
    arr[i],arr[j]=arr[j],arr[i]
    i=i+1
    j=j-1
  elif arr[i]<arr[j]:
    i=i+1
    j=j-1
print(arr)
print(12)