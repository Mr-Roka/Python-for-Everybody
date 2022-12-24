mail_counts ={}
data=input("Enter file name:")
file = open(data)    #Opening the file


for line in file:
    if line.startswith("From "):
        sp = line.split()
        #print(sp)  
        mail = sp[1]
        domain_sp=mail.split("@")
        domain=domain_sp[1]      


        if domain in mail_counts:
            mail_counts[domain] += 1
        else:
            mail_counts[domain] = 1

#print(mail_counts)
# Find the person with the most messages

list=sorted([(count,mail) for mail, count in mail_counts.items()], reverse =True)


most_msg=None

for count,mail in list:
    if most_msg is None or count >most_msg:
        most_msg=count

print(mail, most_msg)
