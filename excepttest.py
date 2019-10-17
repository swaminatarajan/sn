# -*- coding: utf-8 -*-
try :
    city = list()
    with open("D:/realestate2.csv", "r") as fobj:
        header = fobj.readline()
        print(header)
        for line in fobj:
            line = line.strip()
            output = line.split(",")
            city.append(output[1])
            print("------------------------------")
except FileNotFoundError as error:
    print("file not found..Please check")
    print("System error")
except Exception as error:
    print("Error Occured")
    print("System error :", error)
else:
    for item in set(city):
        print(item.ljust(10, '*'), city.count(item), "times")
    
        