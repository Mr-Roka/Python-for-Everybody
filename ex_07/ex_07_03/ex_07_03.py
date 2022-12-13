#Sometimes when programmers get bored or want to have a bit of fun, they add a harmless Easter Egg to 
# their program. Modify the program that prompts the user for the file name so that it prints a funny 
# message when the user types in the exact file name “na na boo boo”. The program should behave normally 
# for all other files which exist and don’t exist. Here is a sample execution of the program:

data =input("Enter the file name: ")

try:
    op=open(data)
except:
    print('File cannot be opened:', data)
    exit()

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