# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

# Pseudocode

# Create a function to define the initial and last number are match
    # If length of lst > 0:
def first_and_second_match(lst):
    if len(lst)>0:
    # Return True if initial and last is match
         return lst[0] == lst [-1]
    # Else, return false
    else:
         return False

# Paste the given first list
first_list = [10, 20, 30, 40, 10]

# First list result
result1 = first_and_second_match(first_list )

    # Print first list
print("First Result is ", result1)

# Paste the given second list
second_list = [75, 65, 35, 75, 30]
#Second list result
result2 = first_and_second_match(second_list )

    # Print second list
print("Second Result is ", result2)

