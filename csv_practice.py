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

# --- Exercise 4 ---
total_revenue = 0
with open("data/sales.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        line_total = price * quantity
        total_revenue += line_total
        print(f"{product}: {quantity} units × ${price:.2f} = ${line_total:.2f}")
print(f"Total revenue: ${total_revenue:.2f}")

# --- Exercise 5 ---
rows_read = 0
rows_written = 0
with open("data/sales.csv", "r", newline="") as infile, \
     open("data/cleaned.csv", "w", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    next(reader)
    writer.writerow(["Product", "Price", "Qty", "Total"])
    for row in reader:
        rows_read += 1
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        line_total = price * quantity
        if line_total > 100:
            writer.writerow([product, f"{price:.2f}", quantity, f"{line_total:.2f}"])
            rows_written += 1
print(f"Rows written: {rows_written} of {rows_read} original rows")

# --- Exercise 6 ---
# csv.reader gives me each row as a list, so I find things by number.
# DictReader lets me use the column name, which is easier to read and I prefer it.
dict_total = 0
with open("data/sales.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])
        line_total = price * quantity
        dict_total += line_total
        print(f"{row['product']}: {quantity} units × ${price:.2f} = ${line_total:.2f}")
print(f"Total revenue (DictReader): ${dict_total:.2f}")
print("Matches Exercise 4:", round(dict_total, 2) == round(total_revenue, 2))

# --- Exercise 7 ---
summary = {}
with open("data/sales.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        name = row["product"]
        line_total = float(row["price"]) * int(row["quantity"])
        summary[name] = summary.get(name, 0) + line_total
for name in sorted(summary):
    print(f"{name}: ${summary[name]:.2f}")

# --- Exercise 8 ---
from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("data/run_log.txt", "a") as log:
    log.write(f"{timestamp} - total revenue: ${total_revenue:.2f}\n")
print("Appended a line to data/run_log.txt")