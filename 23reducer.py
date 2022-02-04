import sys

from collections import defaultdict
res=defaultdict(list)
for line in sys.stdin:
  datalist = line.strip().split('\t')
  if (len(datalist) == 2) : 
    producttype, grossincome = datalist
    
    res[producttype].append(float(grossincome))

avgres=defaultdict(int)
for a,b in res.items():
    avgres[a]=sum(b)/len(b)
for producttype,avggrossincome in avgres.items():
    print(producttype,'\t',avggrossincome)
