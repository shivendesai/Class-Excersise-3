#Written by Shiven Desai
#This program displays my full name
# initialize the array of names
# initialize the array of names
# initialize the array of names
# initialize the array of names
# initialize the array of names
# initialize the array of names
# initialize the array of names
names = ["Alice", "Bob", "Charlie", "David", "Emily"]

# add your first and last name using list comprehension
first_name = "Shiven"
last_name = "Desai"
name_chars = [char for char in first_name] + [char for char in last_name]

# join the characters to create the full name string
full_name = "".join(name_chars)

# print the final result
print(f"Your full name is {full_name}")
