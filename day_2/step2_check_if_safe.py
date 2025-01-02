# Definition: calculate 'safe', assume happy path and previous parsing

parsed_values = [[7, 6, 4, 2, 1], [1, 2, 7, 8, 9], [9, 7, 6, 2, 1], [1, 3, 2, 4, 5], [8, 6, 4, 4, 1], [1, 3, 6, 7, 9]]

for parsed_value in parsed_values:
    print(f"Row being evaluated: {parsed_value}")

    is_increasing = all(parsed_value[i] < parsed_value[i + 1] for i in range(len(parsed_value) - 1))
    print(f"Is increasing: {is_increasing}")

    is_decreasing = all(parsed_value[i] > parsed_value[i + 1] for i in range(len(parsed_value) - 1))
    print(f"Is decreasing: {is_decreasing}")

    differences_valid = all(1 <= abs(parsed_value[i] - parsed_value[i + 1]) <= 3 for i in range(len(parsed_value) - 1))
    print(f"Is delta within range: {differences_valid}")
