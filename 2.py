# def is_palindrome(string):
#     i,j=0,len(string)-1
#     while i<j:
#         if string[i] != string[j]:
#             return False
#         i+=1
#         j-=1
#     return True
# print(is_palindrome("HEllo"))
# list=[1,2,3,4,5]
# lst=tuple(list)
# print(min(lst))

# list=[1,2,3,4,5]
# min=list[0]
# for i in range(1,len(list)):
#     if list[i]<min:
#         min=list[i]
# print(min)


# list=[1,2,3,5,-5,-6]
# list2=[i for i in list if i<0]
# print(list2)
# count=0
# print(['negative' if i<0  else 'positive' for i in list ])

# count1=[count:=count+1 for i in list if i<0]
# print(len(count1))
# from functools import reduce

# def add(num1,num2):
#     return num1+num2
# list=[1,2,34,5,6]
# ans=reduce(add,list)
# print(ans)

# lst=[1,234,56,56,76,98]
# def add(num1):
#     return num1+10

# lst_sum=tuple(map(add,lst))
# print(lst_sum)


# lst=[1,2,3,4,-5]

# def find(num1):
#     if num1<0:
#        return num1
# lst2=list(filter(find,lst))
# print(lst2)

a=56
b=98
while b!=0:
    c=b
    b=a%b
    a=c
print(a)
