sh= float(input("Worked Hours: "))
sr= float(input("Rate Per Hour:"))
if sh<= 40:
    pay=sh*sr
    #print("Regular")
else:
    pay=40*sr +(sh-40)*sr*1.5
    #print("Overtime")
print(pay)