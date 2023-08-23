# variables

# a="sai"
# print(a)

# a,b,c="sai","krupa","nanda"
# print(a,b,c)

# a=b="msk"
# print(a,b)

# list=[1,2,3]
# a,b,c=list
# print(a,b,c)


# '''global & local variables'''
# x="global"

# def func():
#     global x
#     x = "local"
#     print(x)

# func()
# print(x)


# data types

# x=5
# print(type(x))
# x=5.0
# print(type(x))
# x="string"
# print(type(x))
# x=True
# print(type(x))
# x=5j
# print(type(x))

# x=[1,2,3]
# print(type(x))
# x=(1,2,3)
# print(type(x))
# x={1,2,3}
# print(type(x))
# x={"a":1,"b":1}
# print(type(x))

# operators , control flow & looping

list=[1,2,3,11,12,13,25,30]

# sum=0
# for i in list:
#     sum+=i
#     print(i,end=" ")
# print("sum = ",sum)

# for i in list:
#     if i<10:
#         print("num < 10 ",i)
#     elif i>10 and i<20:
#         print("num between 10 - 20 ",i)
#     else:
#         print("num > 20 ",i)

# # same logic using while loop
# i=0
# while i<len(list):
#     if list[i]<10:
#         print("num < 10 ",list[i])
#     elif list[i]>10 and list[i]<20:
#         print("num between 10 - 20 ",list[i])
#     else:
#         print("num > 20 ",list[i])
#     i+=1

# print(list[2:4])
# list.insert(4,33)
# list.append(50)
# list2=["str","abc"]
# list.extend(list2)
# print(list)

# list.remove("str")
# list.pop()
# list.pop(0)
# list.sort()
# print(list)

    
# tuple=("sai","krupa","nanda","viswa","sumit")
# for i in tuple:
#     if "s" in i:
#         print("This string has char s - ",i)
        

set={"string",2,True,3.0,2j}
# for i in set:
#     if type(i) is int:
#         print("integer - ",i)
#     elif type(i) is float:
#         print("float - ",i)
#     elif type(i) is str:
#         print("string - ",i)
#     elif type(i) is bool:
#         print("boolean - ",i)
#     else:
#         print("other data type",type(i))

# set.add("str")
# print(set)
# set.update([5,6,7])
# print(set)
        
# dict={"list":[1,2,3],"tuple":("a","b","c"),"set":{1,"str",2.0}}
# for data in dict:
#     for i in dict[data]:
#         print(i,end=" ")
#     print("")

# x=dict.get("list")
# print(x)
# x=dict.keys()
# print(x)
# x=dict.values()
# print(x)

def sum(list=[2,34]):
    sum=0
    for i in list:
        sum+=i
    print(sum)
sum()
sum([1,2,3,4,5])

def sub(*args):
    sum=0
    for i in args:
        sum-=i
    print(sum)
sub(12,2,3)