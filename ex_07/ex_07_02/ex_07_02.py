data =input("Enter the file name: ")
op= open(data)

sum=0
count=0

for dt in op:
    dx = dt.strip()
    if dx.startswith("X-DSPAM-Confidence"):
        ipso =dx.find(":")
        #print(ipso)
        num_str =dx[ipso+1:]
        #print(num_str)
        num_float = float(num_str)
        #print(num_float)
        sum=sum+num_float
        #print(sum)
        count = count+ 1
        #print(count)
#print("Sum:",sum, "count: ", count, "aerage: ", sum/count)
print("Average spam confidence: ", sum/count)