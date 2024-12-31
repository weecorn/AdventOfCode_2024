# **********************************************************************
# This script calculates the total distance between two lists of numbers 
# read from an input file. The process involves:
#   1. Reading the lists of numbers from the file.
#   2. Sorting each list in ascending order.
#   3. Calculating the absolute difference between corresponding numbers 
#      in the sorted lists.
#   4. Summing up all the differences to find the total distance.
# **********************************************************************

filename="input.txt"
left_list = []
right_list = []
total_distance = 0

# *** Read input list
with open(filename, 'r') as file:
    for line in file:
        left, right = map(int, line.strip().split())
        left_list.append(left)
        right_list.append(right)

# *** Sort lists
left_list.sort()
right_list.sort()

# *** Calculate total distance
for left, right in zip(left_list, right_list):
    total_distance += abs(left - right)

print("Total distance: ", total_distance)


