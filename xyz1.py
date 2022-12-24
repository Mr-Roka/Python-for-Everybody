mail_counts ={}
file = open ('mbox-short.txt')    #Opening the file


for line in file:
    if line.startswith("From "):
        sp = line.split()
        #print(sp)  
        mail = sp[1]
        domain=mail.split("@")
        dom=domain[1]
    print(dom)      
