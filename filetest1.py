with open("D:\info.txt", "w") as fobj:

    for number in range(200, 0, -1) :
        if (number>1) :
           fobj.write(str(number)+ ", ")
        else :
           fobj.write(str(number))
"""          
            

with open("D:\info.txt", "r") as fobj:
    for line in fobj:
        #line =line.strip()
        print(line.strip())
    
       
