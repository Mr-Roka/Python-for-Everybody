sum = 0
count = 0
while True :
    value = input("Enter a number: ")
    if value == "done" :
        break
    try:
        val=float(value)
    except:
        print('Invalid Input')
        continue
    sum +=val
    count +=1
print(sum, count, sum/count)