# list
# collection of data
# data=[2,3,4,5,6,7,8]
# print(data)
# print(type(data))

# 1. can contain any data of any size 
# eg:
# data = [1,2,3,'mohan',[3,4,5],'das',12]
# print(data)

# 2.orderd
# eg:
# a=[1,2,3,4]
# b=[2,3,1,4]
# print(a==b)

# 3.list are indexed 
# list also have [star:stop:step]
# 0 1 2 3 4 5 
# a=[20,21,22,23,24,25,26,27,28,20,21,30,31]
# # list of index
# print(a[2])
# print(a[4:8])
# print(a[0:5:3])
# print(a[4:])
# print(a[:7])
# print(a[::+1])
 
# 4.list are mutable
# list✅- mutable
# sting❌- imutable 
# eg:list 
#    0 ,1 ,2 ,3 ,4
# a=[11,12,13,14,15]
# a[2]='mohan'
# print(a)

# eg:string
#  01234 
# a='mohan'
# a[0]='h'
# print(a)

# list operators
# add -element to list 
# append(item)-to add an element to the end of the list
# eg:append
# a=[11,12,13,14,15]
# a.append('sixteen')
# print(a)

# insert(item)-insert an element to that specific index 
# a=[11,12,13,14,15]
# a.insert(2,'ten')
# print (a)

# remove:-remove the element from the list
# a=[11,12,13,14,15]
# a.remove(12)
# print(a)
# pop(of index)-remove last element from list
# a=[11,12,13,14,15]
# a.pop(0)
# print(a) 

# tuple(cololection of data )
#      (also orderd and indexed)
# differnce b/w list and tuple:-list are mutable and tuple are imutable 
# eg:
a=(1,2,3,'aabid',2,1)
print(a)
print (type(a))