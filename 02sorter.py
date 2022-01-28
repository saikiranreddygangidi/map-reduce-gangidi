n = open("output_location_amount.txt","r")  # open file, read-only
s = open("output_location_amount_sorted.txt", "w") # open file, write
lines = n.readlines()
lines.sort()

for line in lines:
 s.write(line)

n.close()
s.close()
