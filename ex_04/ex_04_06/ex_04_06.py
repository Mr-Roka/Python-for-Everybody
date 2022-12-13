def computepay(hour, rate):
    #print("amtpay", hour, rate)
    if hour<= 40:
        pay_amt=hour*rate
        #print("Regular")
        #print(pay_amt)
    else:
        pay_amt=40*rate +(hour-40)*rate*1.5
        #print("Overtime")
        #print(pay_amt)
    return pay_amt

sh = float(input("Worked Hours: "))
sr = float(input("Rate Per Hour: "))

print("Pay", computepay(sh,sr))