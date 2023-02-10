# print(type("hello"))
# print(type(10))
# print(type(10.5))
# print(type(10j))
# print(type("10"))
# name="rishitha"
# print(name)
# x=10
# print(x)
# print(type(x))
# c=x+20
# print(c)
# a=5//2
# print(a)
# b=5/2
# print(a)
# c=3**5
# print(c)
# name=input("enter the name")
# print("rishitha")
# print(type(name))
# a=10
# b=10
# c=20
# print(a>b)
# print(a==b)
# print(a is not b)
# a=1
# b=0
# print(a or b)
# print(a&b)
# a=10
#  ifa<20:
#    print('fail')
# else:
#    print('pass')
# def myfun(a,b,c):
#     pass
# a=int(input())
# b=int(input())
# c=int(Input())
# d=myfun(a,b,c)
# print(d)
# i=1
# while true: 
#     print(i) 
#     i=i+1
#     if
# for i in "rishitha":
#      print(i,end=" ")
# a="rishitha"
# b=a[-len(a)]
# print(b)        
# for i in a:
#     print(i)

# s="hello world" 
# # print(str[0:10:2])
# # str1="t"+str[1:]
# s1=str.capitalize(s)
# s2=str.split(s)
# s3=str.upper(s)
# print(s1)

# l1=[10,12,30]
# l2=[2,3,4]
# # l.extend(12)
# l1.sort()
# print(l1)
# l=list()
# l1=[1,2,3]
# t[0]=4
# t=tuple(l1)
# print(type(t))

# def reverse(str):
#     str1=""
#     for i in str:
#         str1=i+str1
#     return str1
# s="helloworld"
# print("the original string is:",end="")
# print(str)
# print("the reversed string(using loops)is:",end="")
# print(reverse(s))

# str1=[11,22,33,44,11]
# s=[]
# for i in str1:
#      print("most common elements in string are:",i)
#      print(i(4))
#      s.append(i)
# print("the common elements are:",s)

# def isPalindrome(s):
#     return s==s[::-1]
# s="racecar"
# ans=isPalindrome(s)
# if ans:
#     print("Yes")
# else:
#     print("No")

# x="samarthya"
# w=""
# for i in x:
#     w=i+w
# if(x==w):
#     print("yes")
# else:
#     print("no")
# 
# nterms = int(input("How many terms? "))
# n1, n2 = 0, 1
# count = 0
# if nterms <= 0:
#    print("Please enter a positive integer")
# elif nterms == 1:
#    print("Fibonacci sequence upto",nterms,":")
#    print(n1)
# else:
#    print("Fibonacci sequence:")
#    while count < nterms:
#        print(n1)
#        nth = n1 + n2
#        n1 = n2
#        n2 = nth
#        count += 1












# n = int (input ("Enter the number of digits that you want in the Fibonacci sequence:"))
# n1, n2 = 0, 1
# count = 0
# if n <= 0:
#    print ("The input is invalid. Please enter a positive integer")
# elif n == 1:
#    print("Fibonacci sequence up to n terms will be:")
#    print (n1)
# else:
#    print ("Fibonacci sequence up to the given terms will be:")
# while count < n:
#    print (n1)
#    nth = n1 + n2
#    n1 = n2
#    count = count + 1

# def Fibonacci(n):
#     if n < 0:
#         print("fibonacci sequence upto",nterms,":")
#     elif n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)
# print(Fibonacci(9))

from collections import Counter
s = 'absarbhuadsryjknsvfsrplkhgdsr'
print("Original string: "+s)
print("Most common element in string:")
print(Counter(s).most_common(3))