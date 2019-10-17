ipadd = input("Enter IP Address :")
dipadd = ipadd.split(".")

if (len(dipadd)==4 and dipadd[0].isnumeric() and \
   dipadd[1].isnumeric() and \
   dipadd[2].isnumeric() and \
   dipadd[3].isnumeric()) :
     print(dipadd," Is Valid")
else:
     print(dipadd, " Is invalid")

