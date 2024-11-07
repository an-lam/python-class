import csv
from colorama import Fore, Style

#file_name = "bloomberg-options-Jan7-22.csv"
# file_name = "C:/users/anlam/iclouddrive/home/3stocks/2022-04-30-OpenInterestSpy-col.csv"
file_name = "2022-04-30-OpenInt-test.csv"

with open(file_name, mode='r') as csv_file:
    # csv_reader = csv.DictReader(csv_file)
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(Fore.RED + "Column names: ", ", ".join(row), Style.RESET_ALL)
            line_count += 1

        print("row = ", row)

        """
        print(f'''\t{row["name"]} works in the {row["department"]} department, 
              and was born in {row["birthday month"]}.''')
        """
        line_count += 1

    print(f'Processed {line_count} lines.')