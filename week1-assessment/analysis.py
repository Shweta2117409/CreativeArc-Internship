#step 1
file_path = "data.csv"

file = open(file_path, "r")
lines = file.readlines()
file.close()

print(lines)


#step 2
cleaned_lines = []
for line in lines:
    line = line.strip()
    if line != "":
        cleaned_lines.append(line)

print(cleaned_lines)

#step 3

header_line = cleaned_lines[0]
data_lines = cleaned_lines[1:]

raw_header = header_line.split(",")

header = []
for col in raw_header:
    header.append(col.strip())


print("Cleaned Header:", header)
print("Number of records:" , len(data_lines))

#step 4
data_rows = []
for line in data_lines:
    values = line.split(",")
    data_rows.append(values)

print("First row:", data_rows[0])
print("Total rows:", len(data_rows))

# step 5
missing_values = ["", "NA", "null", "None"]

# step 6
price_index = header.index("PRICE")


price_values = []
missing_price_count = 0

for row in data_rows:
    value = row[price_index].strip()

    if value in missing_values:
        missing_price_count += 1
    else:
        price_values.append(value)

print("Valid PRICE values:", price_values)
print("Missing PRICE count:", missing_price_count)

# step 7
import numpy as np


numeric_prices = []

for value in price_values:
    numeric_prices.append(float(value))

print("Numeric PRICE values:", numeric_prices)


mean_price = np.mean(numeric_prices)
median_price = np.median(numeric_prices)
std_price = np.std(numeric_prices)

print("Mean PRICE:", mean_price)
print("Median PRICE:", median_price)
print("Standard Deviation of PRICE:", std_price)

# step 8

fruit_index = header.index("FRUIT")

fruit_frequency = {}
missing_fruit_count = 0

for row in data_rows:
    fruit = row[fruit_index].strip().lower()

    if fruit in missing_values:
        missing_fruit_count += 1
    else:
        if fruit in fruit_frequency:
            fruit_frequency[fruit] += 1
        else:
            fruit_frequency[fruit] = 1


top_5_fruits = sorted(
    fruit_frequency.items(),
    key=lambda item: item[1],
    reverse=True
)[:5]

print("Top 5 Fruits:", top_5_fruits)

# step 9

with open("summary_report.txt", "w") as report:
    report.write("Column Analyzed: PRICE\n")
    report.write(f"Total Records: {len(data_rows)}\n")
    report.write(f"Missing PRICE Values: {missing_price_count}\n")
    report.write(f"Mean PRICE: {mean_price:.2f}\n")
    report.write(f"Median PRICE: {median_price:.2f}\n")
    report.write(f"Standard Deviation: {std_price:.2f}\n\n")

    report.write("Top 5 Fruits:\n")
    for fruit, count in top_5_fruits:
        report.write(f"{fruit} - {count}\n")

print("Summary report generated successfully.")













