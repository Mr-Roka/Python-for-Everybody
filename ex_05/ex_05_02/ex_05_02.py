largest = None
smallest = None

while True:
    amt = input('Enter A Number: ')
    if amt == 'done':
        break
    try:
        val = int(amt)
    except:
        print("Invalid input")
        continue
    
    if smallest is None:
         smallest = val
    elif val < smallest:
        smallest = val

    if largest is None:
        largest = val
    elif val > largest:
        largest = val


print('Maximum is', largest)
print('Minimum is', smallest)       