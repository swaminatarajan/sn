atup = tuple()
alist = list(atup)

alist.append("unix")

print(alist)

alist.extend(['c','cpp','ja', 'spark', 'scala'])
alist.extend(['hadoop','sccm', 'va','salesforce','sap'])


print(alist)


alist.remove('ja');
print ("List : ", alist)
alist.remove('salesforce');
print ("List : ", alist)

alist.insert(0, 'oracle')
print ("List : ", alist)

alist.insert(5, 'mongodb')
print ("List : ", alist)

alist.reverse()
print ("List : ", alist)

print("alist:", len(alist))

print ("List : ", alist.count("unix"))