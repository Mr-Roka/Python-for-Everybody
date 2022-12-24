# Open the mbox-short.txt file
with open('mbox-short.txt', 'r') as f:
    # Create an empty dictionary to store the counts
    sender_counts = {}

    # Read each line in the file
    for line in f:
        # Check if the line starts with "From"
        if line.startswith('From'):
            # Split the line into words
            words = line.split()
            # Get the sender's email address, which is the fourth word
            sender = words[1]
            # Increment the count for this sender in the dictionary
            if sender in sender_counts:
                sender_counts[sender] += 1
            else:
                sender_counts[sender] = 1
print(sender_counts)
# Find the person with the most messages
most_messages = 0
for sender, count in sender_counts.items():
    if count > most_messages:
        most_messages = count

# Print the result
print(most_messages)
