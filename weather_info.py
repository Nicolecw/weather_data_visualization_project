import csv
from pathlib import Path

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

print(temps)

#for year in temps.keys():
#    for row in reader:
#        if int(row[0]) == year:
#            temp = int(row[2])
#            temps[year].append(temp)