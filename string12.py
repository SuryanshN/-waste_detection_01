# # # # # s="hello"
# # # # # # s=s[::-1]
# # # # # # print(s)
# # # # # s1=list(s)
# # # # # i=0
# # # # # j=len(s1)-1
# # # # # while(i<j):
# # # # #    s1[i],s1[j]=s[j],s[i]
# # # # #    s=str(s1)
# # # # # print(s)

# # # # # s="hello"
# # # # # s1=''
# # # # # i=len(s)-1
# # # # # while(i>=0):
# # # # #     s1+=s[i]
# # # # #     i-=1
# # # # # print(s1)
# # # # # find how manny times a particular letter in string has repeated
# # # # s="test string"
# # # # d=dict()
# # # # # s1=''
# # # # for i in range(len(s)):
# # # #     if  s[i]  in d:
# # # #         d[s[i]]+=1
# # # #     else:
# # # #           d[s[i]]=1
# # # # for i,j in d.items():
# # # #      if(j>1):
# # # #           print(str(i),'count',str(j))

# # # #how manny no of  duplicate element present in the string
# # # # s="hwllo"
# # # # c={}
# # # # for i in range(len(s)):
# # # #     if s[i] in c:
# # # #           c[s[i]]+=1
# # # #     else:
# # # #           c[s[i]]=1
    
# # # # for i,j in c.items():
# # # #      if j>1:
# # # #         print(str(i)+'count='+str(j))

# # # # # checck given string is a rotation of other string
# # # # def f1(string1,string2):
# # # #     s1=len(string1)
# # # #     s2=len(string2)
# # # #     if(s1!=s2):
# # # #         return 0
# # # #     temp=''
# # # #     temp=string1+string2
# # # #     if (temp.count(string2)>0):
# # # #         return 1
# # # #     else:
# # # #         return 0



# # # # string1 = "AACD"
# # # # string2 = "ACDA"
# # # # s1=len(string1)
# # # # s2=len(string2)
# # # # print(f1(string1,string2))
    
# # # # count and say problem
# # # # def cs(s):
# # # #     d={}
# # # #     t=''
# # # #     for i in range(len(s)):
# # # #         if s[i] in d:
# # # #             d[s[i]]+=1
# # # #         else:
# # # #             d[s[i]]=1
# # # #     for i,j in d.items():
# # # #         t+=str(j)
# # # #         t+=str(i)
# # # #     return t
# # # # s='3322251'
# # # # print(cs(s))

# # # # def cs(n):
# # # #     if(n==1):
# # # #         return '1'
# # # #     if(n==2):
# # # #         return '11'
# # # #     s='11'
    
# # # #     for j in range(3,len(s)+1):
# # # #         s=s+'$'
# # # #         c=1
# # # #         t=' '
# # # #         for i in range(1,len(s)):
# # # #             if s[i]!=s[i-1]:
# # # #                 t+=str(c)
# # # #                 t+=s[i-1]
# # # #                 c=1
# # # #             else:
# # # #                 c+=1
# # # #         s=t
# # # #     return s
# # # # n=4
# # # # print(cs(n))
# # # # d='11'
# # # # c={}
# # # # c[d]=len(d)
# # # # print(c)


# # # # def st(s):
# # # #     t=''
# # # #     d={}
# # # #     for i in range(0,len(s)):
# # # #         for j in range(i,len(s)+1):
# # # #             t+=s[i:j]
# # # #             if(t==t[::-1]):
# # # #                 d[t]=len(t)
# # # #                 t=''
# # # #     maxs=-11111111
    
# # # #     for i in d.values():
# # # #         maxs=max(maxs,i)
# # # #     return maxs,d,i,j
        


# # # # s= "aaaabbaa"
# # # # print(st(s))

# # # # def di(d):
# # # #     maxs=-1111111
# # # #     for i in d.values():
# # # #         maxs=max(maxs,i)
# # # #     return maxs

# # # # d={'a':123,'b':9890}
# # # # # print(di(d))
# # # # s='aaa'
# # # # r=''
# # # # r+=s[::]
# # # # print(r)

# # # def longestPalindrome(S):
# # #         start=0
# # #         maxLen=1
# # #         for i in range(1,len(S)):
# # #             #even
# # #             l=i-1 
# # #             r=i   
# # #             print(l,r)
# # #             while l>=0 and r<len(S) and S[l]==S[r]:
# # #                 if r-l+1>maxLen:
# # #                     maxLen=r-l+1
# # #                     start=l
# # #                 l-=1
# # #                 r+=1
# # #             #odd    
# # #             l=i-1
# # #             r=i+1
# # #             while l>=0 and r<len(S) and S[l]==S[r]:
# # #                 if r-l+1>maxLen:
# # #                     maxLen=r-l+1
# # #                     start=l
# # #                 l-=1
# # #                 r+=1    
                
            
# # #         return S[start:start+maxLen]     
# # # s= "aaaabbaa"

# # # print(longestPalindrome(s))

# # # s='abc'
# # # for i in range(len(s)):
# # #     l=s[0:i]
# # #     r=s[i+1:]
# # #     sf=l+r
# # #     print("left="+l,"right="+r,sf)

# # # Split the binary string into substrings with equal number of 0s and 1s

# # # def max_sub_string(s,n):
# # #     c_0=0
# # #     c_1=0
# # #     cnt=0
# # #     for i in range(0,n):
# # #         if s[i]=='0':
# # #             c_0+=1
# # #         else:
# # #             c_1+=1
# # #         if c_0==c_1:
# # #             cnt+=1
# # #     if c_0!=c_1:
# # #         return -1
# # #     return cnt
# # # s="01010011"
# # # n=len(s)
# # # print(max_sub_strin


# # # Edit Distance
# # # def edit_distance(s1,s2,m,n):
# # #     dp=[[0 for x in range(n+1)] for x in range(m+1)]
# # #     for i in range(m+1):
# # #         for j in range(n+1):
# # #             if i==0:
# # #                 dp[i][j]=j
# # #             elif j==0:
# # #                 dp[i][j]=i
# # #             elif s1[i-1]==s2[j-1]:
# # #                     dp[i][j]=dp[i-1][j-1]
# # #             else:
# # #                 dp[i][j]=1+min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
# # #     return dp[m][n]
# # # s1="sunday"
# # # s2="saturday"
# # # m=len(s1)
# # # n=len(s2)
# # # print(edit_distance(s1,s2,m,n))

# # # dp=[[0 for x in range(8)] for x in range(6)]
# # # print(dp)

# # # # next permutation
# # # def perm(arr):
# # #     i=0
# # #     j=0
# # #     n=len(arr)
# # #     for i in range(n-2,-1,-1):
# # #         if(arr[i]<arr[i+1]):
# # #             break
# # #     if(i<0):
# # #         i.reverse()
# # #     else:

# # #         for j in range(n-1,i,-1):
# # #             if(arr[j]>arr[i]):
# # #                 break
# # #         arr[i],arr[j]=arr[j],arr[i]
# # #         s,e=i+1,len(arr)
# # #         arr[s:e]=arr[s:e][::-1]
    

# # # arr=[1,2,3,6,5,4]
# # # perm(arr)
# # # for i in arr:
# # #     print(i)


# # # longest prefix suffix
# # ''' i longest prefix and suffix first we divide the string in equal part then we check it left part is equal to right part if it is equal then we calculate the size of 1 side of string and show it is a longest prefix suffix'''

# # def lps(s):
# #     n=len(s)
# #     for res in (n//2,0,-1):
# #         prefix= s[0: res]
# #         suffix=s[n-res: n]
        
# #         if(prefix == suffix):
# #             return res
    
# #     return 0

# # s = "blablabla"
# # print(lps(s))

# # # def longestPrefixSuffix(s) :
# # #     n = len(s)
     
# # #     for res in range(n // 2, 0, -1) :
         
# # #         # Check for shorter lengths
# # #         # of first half.
# # #         prefix = s[0: res]
# # #         suffix = s[n - res: n]
         
# # #         if (prefix == suffix) :
# # #             return res
             
 
# # #     # if no prefix and suffix match
# # #     # occurs
# # #     return 0
     
# # # # Driver Code
# # # if __name__ == "__main__":
# # #     s = "blablabla"
# # #     print(longestPrefixSuffix(s))
# # N=6
# # cps = [[0 for i in range(N)]for j in range(N + 2)]
# # print(cps)


# def first(arr, x, n):
 
#     low = 0
#     high = n - 1
#     res = -1
 
#     while (low <= high):
 
#         # Normal Binary Search Logic
#         mid = (low + high) // 2
 
#         if arr[mid] > x:
#             high = mid - 1
#         elif arr[mid] < x:
#             low = mid + 1
 
#         # If arr[mid] is same as x, we
#         # update res and move to the left
#         # half.
#         else:
#             res = mid
#             high = mid - 1
 
#     return res
 
# # If x is present in arr[] then returns
# # the index of FIRST occurrence of x in
# # arr[0..n-1], otherwise returns -1
 
 
# def last(arr, x, n):
 
#     low = 0
#     high = n - 1
#     res = -1
 
#     while(low <= high):
 
#         # Normal Binary Search Logic
#         mid = (low + high) // 2
 
#         if arr[mid] > x:
#             high = mid - 1
#         elif arr[mid] < x:
#             low = mid + 1
 
#         # If arr[mid] is same as x, we
#         # update res and move to the Right
#         # half.
#         else:
#             res = mid
#             low = mid + 1
 
#     return res
 
 
# # Driver code
# arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
# n = len(arr)
# x = 8
 
# print("First Occurrence =", first(arr, x, n))
# print("Last Occurrence =", last(arr, x, n))
def indexes( v, x):
        # Your code goes here
        l=0
        h=len(v)-1
        Lres=-1
        Rres=-1
        while(l<=h):
            mid=(l+h)//2
            if(v[mid]>x):
                h=mid-1
            elif(v[mid]<x):
                l=mid+1
            else:
                Lres=mid
                h=mid-1
        1.pul=0
        h=len(v)-1
        while(l<=h):
            mid=(l+h)//2
            if(v[mid]>x):
                h=mid-1
            elif(v[mid]<x):
                l=mid+1
            else:
                Rres=mid
                l=mid+1
        return  Lres,Rres
v=[1, 3, 5, 5, 5, 5 ,67 ,123 ,125]
x=5
print(indexes(v,5))