import csv

def read_csv_file(filename):
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(', '.join(row))

# Example usage
filename = 'data.csv'
print(f"Contents of '{filename}':")
read_csv_file(filename)

