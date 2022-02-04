import sys 

for line in sys.stdin:
  datalist = line.strip().split("    ")
  datalist=datalist[0].split(",")
  
  if (len(datalist) == 17) : 
    invoice,branch, city,CustomerType, gender, producttype, unitprice,Quality,Tax,Total,date,time,payment,cogs,grossmperc,grossincome,rating = datalist

    print(producttype,"\t",grossincome)
