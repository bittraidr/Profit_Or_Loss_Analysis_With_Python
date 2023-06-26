import csv

menu_filepath = 'menu_data.csv'
sales_filepath = 'sales_data.csv'

menu = []
sales = []

# use with statement and open menu_data.csv from file path
with open(menu_filepath, 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        menu.append(row)

# with statement to open sales_data.csv
with open(sales_filepath, 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        sales.append(row)

# initialize empty report dictionary
report = {}

# Loop through every row in the sales data
for row in sales:
    quantity = int(row[3])
    menu_item = row[4]

    # Check if sales_item is already included in the report
    if menu_item not in report:
        # Initialize key-value pairs for the sales_item in the report
        report[menu_item] = {
            '01-count': 0,
            '02-revenue': 0,
            '03-cogs': 0,
            '04-profit': 0
        }

    # Create nested loop by looping through every record in menu
    for menu_row in menu:
        item = menu_row[0]
        price = float(menu_row[3])
        cost = float(menu_row[4])

        if menu_item == item:
            profit = price - cost

            # Cumulatively add the values to the corresponding metrics in the report
            report[menu_item]['01-count'] += quantity
            report[menu_item]['02-revenue'] += price * quantity
            report[menu_item]['03-cogs'] += cost * quantity
            report[menu_item]['04-profit'] += profit * quantity
        # else:
        #     print(f'{menu_item} does not equal {item}! NO MATCH!')

# Write out the contents of the report
with open('report.txt', 'w') as file:
    for item, metrics in report.items():
        file.write(f'{item}\n')
        for metric, value in metrics.items():
            file.write(f'{metric}: {value}\n')
        file.write('\n')
