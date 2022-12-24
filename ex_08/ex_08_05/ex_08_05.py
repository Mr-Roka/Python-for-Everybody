#Defining the Vatibles
unique_mail=[]
count=0
# Open the File
with open('mbox-short.txt') as op_file:

    for data in op_file:
        #finding the email int the file starting eith from:
        if data.startswith('From:'):
            sp_data=data.split()
            sp_email=sp_data[1]
            #print the email
            print(sp_email)
            count+=1
# printing the Count    
print("There were",count, "lines in the file with From as the first word")