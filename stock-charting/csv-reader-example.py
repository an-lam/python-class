import csv

file_name8 = "2022-05-04-SPY.csv"

options = []
already_print = False
with open(file_name8, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        # data = re.split('" |, |\n', line.strip())
        # if line_count == 0:
        if ("Exp" in row) or ("<empty>" in row):
            if not already_print:
                print(Fore.RED + "Column names: ", ", ".join(row), Style.RESET_ALL)
                already_print = True
        else:
            #print("row = ", row)
            if row and row[0] != '':
                record = tuple(row)
                # print("record: ", record)
                options.append(record)
        line_count += 1

print("lines_count = ", line_count)

