import matplotlib.pyplot as plt
import Grid
import csv

data_file = "data.csv"
size = 2;

# take data from csv
with open(data_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)  
    list_of_csv = list(csvreader)
print(list_of_csv)

list_of_paths = []
for row in list_of_csv:
    path = Grid.PathData(row[0], row[1], row[2], row[3], row[4])
    list_of_paths.append(path)



# create graph
fig, ax = plt.subplots()

for x in range(size): # create dot grid
    for y in range(size):
        ax.plot(x, y, "ko")

# plot data
for path in list_of_paths:
    ax.plot([path.x1, path.x2], [path.y1, path.y2], path.get_color(), linewidth=4)

ax.set_aspect("equal")
plt.show()


