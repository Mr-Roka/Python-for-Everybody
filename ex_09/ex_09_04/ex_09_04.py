mail_counts ={}
data=input("Enter file name:")
file = open(data)    #Opening the file


for line in file:
    if line.startswith("From "):
        sp = line.split()
        #print(sp)  
        mail = sp[1]      


        if mail in mail_counts:
            mail_counts[mail] += 1
        else:
            mail_counts[mail] = 1

#print(mail_counts)
# Find the person with the most messages

print(mail_counts)
most_msg = None
most_msg_by=None
for mail, count in mail_counts.items():
    if most_msg is None or count > most_msg:
        most_msg = count
        most_msg_by=mail
    
print(most_msg_by, most_msg)
    