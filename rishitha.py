def reverse(str):
    str1=""
    for i in str:
        str1=i+str1
    return str1
s="helloworld"
print("the original string is:",end="")
print(str)
print("the reversed string(using loops)is:",end="")
print(reverse(s))