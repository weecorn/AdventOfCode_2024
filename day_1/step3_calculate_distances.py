# Definition: Calculate difference between elements from both lists.

sorted_left_list = [1, 2, 3, 3, 3, 4]
sorted_right_list = [3, 3, 3, 4, 5, 9]
delta_left_right = []

for left, right in zip(sorted_left_list, sorted_right_list):
    delta_left_right.append(abs(left - right))

print(delta_left_right)




