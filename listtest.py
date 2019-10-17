# -*- coding: utf-8 -*-
name = "python programming"

print(len(name))

alist =[10,20,30]
print(len(alist))

atup = ("perl", "java")
print(len(atup))


alist = [10,20,30]

alist.append(40)
print("After appending :", alist)

adict ={"chap1":10, "chap2":20}

print(adict)

print(adict.keys())

print(adict.values())

print(adict.items())

print(adict.get("chap3", "onnumilla"))

bdict = {"chap4":40}
adict.update(bdict)
print("After update :", adict)

aset = {"google.com","google.com","linkedin.com"}
bset = {"google.com","facebook.com"}


print(aset.union(bset))
print(aset.intersection(bset))

print(aset.issubset(bset))

print(aset.difference(bset))
print(bset.difference(aset))


name = input("name:")
print(name)

print(len(name))

print(list(range(1,10)))