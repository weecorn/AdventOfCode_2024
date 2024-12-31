# Definition: read input file, assume hhappy path.
#   For each row, read two numbers: left and right (as per problem outline)

filename="sample_input.txt"
left_list = []
right_list = []

with open(filename, 'r') as file:
    for line in file:
        left, right = map(int, line.strip().split())
        left_list.append(left)
        right_list.append(right)

print(left_list)
print(right_list)