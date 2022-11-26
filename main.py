import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

colors = ["Gray", "Cinnamon", "Black"]
count = []

for color in colors:
    count.append(len(data[data["Primary Fur Color"] == color]))

sub_data = pandas.DataFrame(
    {
        "Fur Color": colors,
        "Count": count,
    }
)

sub_data.to_csv("Squirrel count.csv")
print(sub_data)
