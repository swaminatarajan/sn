import csv
with open("d:/realestate2.csv","r") as fobj:
    reader = csv.reader(fobj)
    for line in reader:
        print(line)
        
        
##earlier we were using the below######
with open("d:/realestate2.csv","r") as fobj:
    for line in fobj:
        line = line.strip()
        output = line.split(",")
        print(output)
        
