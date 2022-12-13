hour=input("Worked Hours: ")
rate= input("Rate Per Hour:")
try:
    sh=float(hour)
    sr=float(rate)
except:
    print("Error, please enter numeric input")
    quit()
if sh<= 40:
    pay=sh*sr
    #print("Regular")
else:
    pay=40*sr +(sh-40)*sr*1.5
    #print("Overtime")
print(pay)