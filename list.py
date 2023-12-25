# create an Empty list 
my_list = []

# Add Multiples values to the list:
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(2) # Adding a Duplicate value
my_list.append(4)
my_list.append(1) # Adding another duplicate value

# Remove duplicate from the list
unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)

# print the final list without duplicates:
print("Original list:", my_list)
print("Final list without duplicate:", unique_list) 
