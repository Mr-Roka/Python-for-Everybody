numbers = []  # create an empty list to store the numbers

while True:
    number = input("Enter a number (or 'done' to finish): ")
    if number == "done":
        break # stop the loop when the user enters "done"
    try:
        num=float(number)
    except:
        print("Invalid Input !!")
        continue
    numbers.append(num)  # convert the number to an integer and add it to the list

# use the max() and min() functions to find the maximum and minimum numbers in the list
max_num = max(numbers)
min_num = min(numbers)

# print the results
print("Maximum number:", max_num)
print("Minimum number:", min_num)


xy=input("If you want to look the Numbers you entered, Type Y and Enter:")
if xy == "Y":
    print(numbers)
else:
    exit
