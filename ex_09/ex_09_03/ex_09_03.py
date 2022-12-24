day_counts ={}
data=input("Enter file name:")
file = open(data)    #Opening the file


for line in file:
    if line.startswith("From "):
        sp = line.split()
        #print(sp)
        try:    
            day = sp[1]      #3rd word of the line which is day of the week ie, sat, fri
        except:
            day=None
        #print(day)


        if day in day_counts:
            day_counts[day] += 1
        else:
            day_counts[day] = 1


print(day_counts)