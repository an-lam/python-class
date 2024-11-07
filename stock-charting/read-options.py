import csv
from colorama import Fore, Style
import re
import functools

# for plotting
import matplotlib.pyplot as plt

# Compare call open interest
def compare_call(x, y):
    oix = int(str(x[1]).replace(',', ''))
    oiy = int(str(y[1]).replace(',', ''))

    return 1 if oix < oiy else -1

# Compare put open interest
def compare_put(x, y):
    # oix = int(str(x[9]).replace(',', ''))
    # oiy = int(str(y[9]).replace(',', ''))
    oix = int(str(x[13]).replace(',', ''))
    oiy = int(str(y[13]).replace(',', ''))
    return 1 if oix < oiy else -1

def sort_tuple(tup, put=True):
    # reverse = None (Sorts in Ascending order)
	# key is set to sort using second element of
	# sublist lambda has been used
    # tup.sort(key = lambda x: x[2], reverse = True)
    if put:
        #tup.sort(key = functools.cmp_to_key(compare_put))
        result = sorted(tup, key = functools.cmp_to_key(compare_put))
    else:
        #tup.sort(key = functools.cmp_to_key(compare_call))
        result = sorted(tup, key = functools.cmp_to_key(compare_call))
    return result

def plot_charts(options, put=True):
    # creating the dataset
    if put:
        column = 9
        bar_color = "red"
        title = "Top PUT Open Interest"
    else:
        column = 1
        bar_color = "green"
        title = "Top CALL Open Interest"

    oi = []
    exp = []
    for i in range(0, 9):
        oi.append(int(str(options[i][column]).replace(',', '')))
        exp_strike = str(options[i][4])[:6] + " " + str(options[i][5])
        exp.append(exp_strike)

    #print(" oi = ", oi)
    #print(" exp = ", exp)

    fig = plt.figure(figsize=(12, 5))
    # creating the bar plot
    plt.bar(exp, oi, color=bar_color,
            width=0.3)
    plt.xlabel("Expiration and strikes")
    plt.ylabel("No. of contracts")

    plt.title(title)
    plt.show()

    """
    fig2 = plt.figure(figsize=(5, 5))
    # creating the bar plot
    plt.bar(exp, oi, color=bar_color,
            width=0.3)
    plt.xlabel("Expiration and strikes")
    plt.ylabel("No. of contracts")

    plt.title(title)
    plt.show()
    """

def plot_charts2(put_options, call_options):
    put_oi = []
    put_exp = []
    call_oi = []
    call_exp = []
    for i in range(0, 11):
        # put_oi.append(int(str(put_options[i][9]).replace(',', '')))
        put_oi.append(int(str(put_options[i][13]).replace(',', '')))
        # exp_strike = str(options[i][4])[:6] + " " + str(options[i][5])
        exp_strike = str(put_options[i][6])[:6] + " " + str(put_options[i][7])
        put_exp.append(exp_strike)

        call_oi.append(int(str(call_options[i][1]).replace(',', '')))
        #exp_strike = str(call_options[i][4])[:6] + " " + str(call_options[i][5])
        exp_strike = str(call_options[i][6])[:6] + " " + str(call_options[i][7])
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
file_name = "C:/users/anlam/iclouddrive/home/3stocks/2022-04-30-OpenInterestSpy-col.csv"
file_name2 = "2022-04-30-OpenInt-test.csv"
file_name3 = "2022-05-02-QQQ.csv"
file_name4 = "2022-05-02-tos-IWM.csv"
file_name5 = "2022-05-04-DIA2.csv"
file_name6 = "2022-05-04-IWM.csv"
file_name7 = "2022-05-04-QQQ.csv"
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

# Sort the put IO
#print("options = ", options)

put_list = sort_tuple(options)
#print("sorted PUT options = ", options)
print("Top 10 OI PUTs: \n i \t data ")
for i in range(0, 14):
    print(i, put_list[i])

#plot_charts(put_list)

call_list = sort_tuple(options, False)
# print("\n sorted CALL options = ", options)
print("\n Top 10 OI CALLs: \n i \t data ")
for i in range(0, 14):
    print(i, call_list[i])

#plot_charts(call_list, False)
plot_charts2(put_list, call_list)

print("done")