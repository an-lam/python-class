# Import the modules
import matplotlib.pyplot as plt

# Initialize a dictionary for months
data = dict()

# Read the data
with open('electronics.csv', 'r') as f:
    for line in f.readlines():

        # Store each line in the dictionary
        month, item, quantity = line.split(',')

        if month not in data:
            data[month] = []
        data[month].append((item, int(quantity)))

# Position of each subplot where 221 means 2 row,
# 2 columns, 1st index
positions = [221, 222, 223, 224]

# Colors to distinguish the plot
colors = ['r', 'g', 'b', 'y']

# Plot the subgraphs
for i, l in enumerate(data.keys()):
    plt.subplot(positions[i])
    data_i = dict(data[l])
    plt.bar(data_i.keys(), data_i.values(), color=colors[i])
    plt.xlabel(l)

# Show the plots
plt.show()
