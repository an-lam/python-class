import sys

import threading
import csv
from colorama import Fore, Style
import re
import functools

# for plotting
import matplotlib.pyplot as plt

# for selecting file
from tkinter.filedialog import askopenfilename
# from tkinter.filedialog import asksaveasfilename

def select_file():
    file_selected = askopenfilename()
    print("You selected: ", file_selected)

    csv_file = file_selected.replace("-StockAndOptionQuoteFor", "-")
    print("csv_file = ", csv_file)
    output_fh = open(csv_file, 'w')

    # Check the file to see if it not CSV, then delete non-csv line
    # and create a new CSV file with shorter name
    input_fh = open(file_selected, 'r')
    for line in input_fh:
        # is_csv = re.search("^,,", line)
        # if line.find(",,") == 0 and line.find("empty") == -1:
        if line.find(",,") == 0:
            clean_line = line.replace(",,", '')
            output_fh.write(clean_line)

    output_fh.close()
    input_fh.close()
    # Use regular expression to check for ",,Volume,Open Int.,"

    return csv_file


def sort_tuple(in_opt_list, key_index):
    neednextpass = True
    k = 1
    opt_list = in_opt_list.copy()

    while k < len(opt_list) and neednextpass:
        neednextpass = False
        for i in range(len(opt_list) - k):
            # Need to fix this
            current = int(str(opt_list[i][key_index]).replace(',', ''))
            next = int(str(opt_list[i+1][key_index]).replace(',', ''))
            if current < next:
                opt_list[i], opt_list[i+1] = opt_list[i+1], opt_list[i]
                neednextpass = True
        k+=1

    return opt_list

def plot_charts2(put_options, put_oi_ix, call_options, call_oi_ix, strike_ix):
    put_oi = []
    put_exp = []
    call_oi = []
    call_exp = []
    for i in range(0, 11):
        # put_oi.append(int(str(put_options[i][9]).replace(',', '')))
        put_oi.append(int(str(put_options[i][put_oi_ix]).replace(',', '')))
        # exp_strike = str(options[i][4])[:6] + " " + str(options[i][5])
        # exp_strike = str(put_options[i][6])[:6] + " " + str(put_options[i][7])
        exp_strike = str(put_options[i][strike_ix])[:strike_ix-1] + "-" + str(put_options[i][strike_ix-1])
        put_exp.append(exp_strike)

        call_oi.append(int(str(call_options[i][call_oi_ix]).replace(',', '')))
        #exp_strike = str(call_options[i][4])[:6] + " " + str(call_options[i][5])
        exp_strike = str(call_options[i][strike_ix])[:strike_ix] + "-" + str(call_options[i][strike_ix-1])
        call_exp.append(exp_strike)


    #print(" oi = ", oi)
    #print(" exp = ", exp)

    fig = plt.figure(figsize=(14, 5))
    # creating the bar plot
    plt.bar(put_exp, put_oi, color="red",
            width=0.15)
    plt.xlabel("Expiration and strikes")
    plt.ylabel("No. of contracts")
    plt.title("Put Options")

    fig2 = plt.figure(figsize=(14, 5))
    # creating the bar plot
    plt.bar(call_exp, call_oi, color="green",
            width=0.15)
    plt.xlabel("Expiration and strikes")
    plt.ylabel("No. of contracts")
    plt.title("Call Options")
    plt.show()


# ----------------- main program ----------------
#file_name = "bloomberg-options-Jan7-22.csv"
file_2_process = select_file()

# sys.exit()

options = []
already_print = False
with open(file_2_process, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        # data = re.split('" |, |\n', line.strip())
        # if line_count == 0:
        if ("Exp" in row) or ("<empty>" in row):
            if not already_print:
                print(Fore.RED + "Column names: ", ", ".join(row), Style.RESET_ALL)
                already_print = True
                print("row =", row)
                call_oi_col = row.index("Open.Int")
                put_oi_col = row.index("Open.Int", 5, len(row))
                strike_ix = row.index("Strike")
                print("call_oi_col =", call_oi_col, "\t put_oi_col = ", put_oi_col, "strike_ix = ", strike_ix)
        else:
            #print("row = ", row)
            if row and row[0] != '':
                record = tuple(row)
                # print("record: ", record)
                options.append(record)
        line_count += 1

print("lines_count = ", line_count)

# Sort the put IO
#print("options = ", options)

put_list = sort_tuple(options, put_oi_col)
#print("sorted PUT options = ", options)
print("Top 10 OI PUTs: \n i \t data ")
for i in range(0, 14):
    print(i, put_list[i])

#plot_charts(put_list)

call_list = sort_tuple(options, call_oi_col)
# print("\n sorted CALL options = ", options)
print("\n Top 10 OI CALLs: \n i \t data ")
for i in range(0, 14):
    print(i, call_list[i])

#plot_charts2(put_list, put_oi_col, call_list, call_oi_col, strike_ix)
""""
daemon=True: run thread as daemon so that it continues to run 
after main thread exits
"""
plot_th = threading.Thread(name='Plot thread', args=(put_list, put_oi_col, call_list, call_oi_col, strike_ix),
                     target=plot_charts2, daemon=True)
plot_th.start()

print("done")
plot_th.join()