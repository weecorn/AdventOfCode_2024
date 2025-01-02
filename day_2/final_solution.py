# Definition: read input file, assume happy path.
def is_safe(report):
    """
    Check if a report is safe.
    A report is safe if:
    - All levels are either strictly increasing or strictly decreasing.
    - All adjacent levels differ by at least 1 and at most 3.
    """
    is_increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    is_decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))
    differences_valid = all(1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))
    
    return (is_increasing or is_decreasing) and differences_valid


def count_safe_reports(filename):
    """
    Read input from a file and count the number of safe reports.
    """
    with open(filename, "r") as file:
        # Parse the input into a list of reports (each report is a list of integers)
        reports = [[int(level) for level in line.split()] for line in file if line.strip()]
    
    # Count the number of safe reports
    safe_count = sum(1 for report in reports if is_safe(report))
    return safe_count


# Path to the input file
input_file = "input.txt"

# Calculate and print the number of safe reports
safe_report_count = count_safe_reports(input_file)
print(f"Number of safe reports: {safe_report_count}")
