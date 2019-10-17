# -*- coding: utf-8 -*-
book = {"chap1":10, "chap2":20, "chap3":30}

print(book)

print(book["chap1"])
print(book["chap2"])

book = {"chap1":10, "chap2":20, "chap3":30, "chap1":'scala'}
print(book["chap1"])

info={1:2,3:4,5:6}

aset = {10,20,30,40,50,30,30}
print(aset)

name = "python programming"

print(name.center(40,"*"))

print(name.count('p'))

print(name.title())

output = name.split("o")
print("After split() :", output)

name = "I love {} and {}"
print(name.format("unix", "java"))
print(name.format(1,2))
print(name.format("java",1))

alist =["unix","java"]
line =".".join(alist)
print("After converting :",line)

name = "python programming"
print(name.replace("python","ruby"))