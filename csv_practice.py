# --- Exercise 1 ---
with open("data/sales.csv", "r") as f:
    print("Opened successfully")

# --- Exercise 2 ---
import csv
with open("data/sales.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# --- Exercise 3 ---
with open("data/sales.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    print("Header:", header)
    for row in reader:
        print(row)