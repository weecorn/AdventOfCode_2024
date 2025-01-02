# Definition: split values from input, assume happy path.

example_input = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

# for line in example_input.strip().split("\n"):
#     print(line)

reports = [[int(level) for level in line.split()] for line in example_input.strip().split("\n")]
 
print(reports)
