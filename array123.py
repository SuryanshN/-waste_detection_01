# def sum_0(arr,n):
#     i=0
#     while(i!=n):
#         sums=0
#         i=0
#         while(i!=n):
#             sums+=arr[i]
#             if(sums==0):
#                 return "Yes"
#             i=i+1
#         i=i+1
#     return "No"
# arr=[4,2,-3,1,6]
# n=len(arr)
# print(sum_0(arr,n))

# python3 program to find if
# there is a zero sum subarray
# def sum_0(arr,n):
#     s=set()
#     sum_n=0
#     for i in range(0,n):
#         sum_n+=arr[i]
#         if(sum_n==0 or sum_n in s):
#             return True
#         s.add(sum_n) 
#     return False
# arr=[4,2,-3,1,6]
# n = len(arr)
 
#     # Function call
# if sum_0(arr, n) == True:
#         print("Found a sunbarray with 0 sum")
# else:
#         print("No Such sub array exits!")

'''Maximum Product Subarray'''
def max_product(arr,n):
    res=arr[0]
    for i in range(0,n):
        m=arr[i]
        for j in range(i+1,n):
            res=max(res,m)
            m*=arr[j]
        res=max(res,m)
    return res
    
arr=[1,-2,-3,0,7,-8,-2]
n=len(arr)
print(max_product(arr,n))
