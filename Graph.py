import matplotlib.pyplot as plt
import Grid
import csv

data_file = "data.csv"
size = 50;

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
    ax.plot([x, x], [0, size], "black", linewidth=1)
    ax.plot([0, size], [x,x], "black", linewidth=1)
    for y in range(size):
        ax.plot(x, y, "ko", markersize=(int(10*1/size))+3)

# plot data
for path in list_of_paths:

    ax.plot(path.x1, path.y1, path.get_color(), marker='o', markersize=(int(15*1/size))+5)
    ax.plot(path.x2, path.y2, path.get_color(), marker='o', markersize=(int(15*1/size))+5)

    for line in path.get_lines():
        ax.plot([line.x1, line.x2], [line.y1, line.y2], path.get_color(), linewidth=2)

ax.set_aspect("equal")
plt.show()


