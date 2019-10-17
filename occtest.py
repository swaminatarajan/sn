data = ["perl","unix","perl","scala","perl"]

uniqueKeys = set(data)

print("data", data)
print("uniqueKeys", uniqueKeys)

for key in uniqueKeys:
   print(key," - " ,data.count(key))

"""
print("Unix", data.count("unix"))
print("scala", data.count("scala"))
print("perl", data.count("perl"))
print("perl", data.count("perl"))
"""
