# Take the following Python code that stores a string:

# str = 'X-DSPAM-Confidence:0.8475'

# Use find and string slicing to extract the portion of the string after 
# the colon character and then use the float function to convert the extracted string 
# into a floating point number.


str = 'X-DSPAM-Confidence:0.8475'

# find the position:
ipso= str.find(":")

#display the part from the above point to the last
num_str=str[ipso+1:]

#converting the string into float
num_float= float(num_str)

print(num_float)
