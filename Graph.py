from Xlib.ext.damage import DamageReportDeltaRectangles
import matplotlib.pyplot as plt
import Grid
import csv

data_file = "data.csv"
size_x = 4
size_y = 6
avg_size = (size_x+size_y)/2

# take data from csv
with open(data_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)  
    list_of_csv = list(csvreader)
print(list_of_csv)

list_of_paths = []
list_of_resistances = []
for row in list_of_csv:
    path = Grid.PathData(row[0], row[1], row[2], row[3], row[4])
    list_of_resistances.append(row[0])
    list_of_paths.append(path)


# create graph
fig, ax = plt.subplots()
ax.set_xlim(0,size_x)
ax.set_ylim(0,size_y)
ax.add_patch(plt.Rectangle((0,6), 10, 10,facecolor='silver', clip_on=False,linewidth = 0))
for x in range(size_x): # create dot grid
    ax.plot([x, x], [0, size_y], "black", linewidth=1)
    ax.plot([0, size_x], [x,x], "black", linewidth=1)
    for y in range(size_y):
        ax.plot(x, y, "ko", markersize=int(10*1/avg_size+3))
    
# plot data

lowest_resistance = min(list_of_resistances) #used for determining line color
highest_resistance = max(list_of_resistances)
for path in list_of_paths:
    
    ax.plot(path.x1, path.y1, path.get_color(), marker='o', markersize=(int(15*1/avg_size))+5)
    ax.plot(path.x2, path.y2, path.get_color(), marker='o', markersize=(int(15*1/avg_size))+5)

    for line in path.get_lines():
        ax.plot([line.x1, line.x2], [line.y1, line.y2], path.get_color(), linewidth=2)

ax.set_aspect("equal")
plt.show()


