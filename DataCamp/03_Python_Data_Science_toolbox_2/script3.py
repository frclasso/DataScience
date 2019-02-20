#!/usr/bin/env python3


doctor = ['house', 'cuddy', 'chase','thirteen', 'wilson']

print([doc[0] for doc in doctor])

#Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member for member in fellowship if len(member) >= 7 ]

# Print the new list
print(new_fellowship)


new_fellowship = [member if len(member) >= 7 else '' for member in fellowship]
print(new_fellowship)


