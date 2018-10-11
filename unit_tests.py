#Template for Outputting Compatible JSON file
import json
import ez_plot

#Prep data structure with data AND formatting options
x = [10000,12000,15000]
y = [10000,12000,15000]

#Create ez_plot data structure
data = ez_plot.returnEZ_Data()
data["xdata"] = x
data["ydata"] = y
data["title"] = "Custom Title"
data["rcparams"]["axes.grid"] = True
#For scientific notation
data["rcparams"]["axes.formatter.limits"] = (-3,3)
print(data)

#Dump data to json file
with open("test.json",'w') as fp:
    json.dump(data,fp)
