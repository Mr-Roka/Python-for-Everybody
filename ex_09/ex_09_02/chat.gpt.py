# Open the mbox-short.txt file
with open('mbox-short.txt', 'r') as f:
    # Create an empty dictionary to store the counts
    day_counts = {}

    # Read each line in the file
    for line in f:
        # Check if the line starts with "From"
        if line.startswith("From "):
            # Split the line into words
            words = line.split()
            # Get the third word, which is the day of the week
            day = words[2]
            # Increment the count for this day in the dictionary
            if day in day_counts:
                day_counts[day] += 1
            else:
                day_counts[day] = 1

# Print the contents of the dictionary
for day, count in day_counts.items():
    print(day_counts)
