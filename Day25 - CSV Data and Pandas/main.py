import csv
import pandas
from numpy import average

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         print(row)
#     print(temperatures)

data = pandas.read_csv("weather_data.csv")
temp_list = data["temp"].to_list()
print(average(temp_list))
print(data["temp"].max())