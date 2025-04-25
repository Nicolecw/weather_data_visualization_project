import csv
from pathlib import Path
import matplotlib.pyplot as plt

path = Path('weather_data.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

temps = {}

for i in range(2015,2025):
    temps[i] = []

for row in reader:
    year = int(row[0])
    temp = int(row[2])
    for key in temps.keys():
        if key == year:
            temps[year].append(temp)

dates = ["July 18",
         "July 19",
         "July 20",
         "July 21",
         "July 22",]

colors = ["red",
          "green",
          "blue",
          "cyan",
          "magenta",
          "orange",
          "yellow",
          "black",
          "purple",
          "maroon"]

for year, color in zip(range(2015,2025), colors):
        plt.plot(dates, temps[year], linestyle='--', marker='o', color=color, label=year)
plt.title('10 Years of Temperatures')
plt.xlabel('Dates')
plt.ylabel('Temperature (Degrees Fahrenheit)')
plt.legend()
plt.grid(True)
plt.show()



#plt.plot(year, temp, linestyle='-', marker='o', color='red', label='Data')
#plt.title('Temperature')
#plt.xlabel('Year')
#plt.ylabel('Temp')
#plt.legend()
#plt.grid(True)
#plt.show()
