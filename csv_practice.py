# --- Exercise 1 ---
with open("data/sales.csv", "r") as f:
    print("Opened successfully")

# --- Exercise 2 ---
import csv
with open("data/sales.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)