from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Open the file in read mode
path = Path("weather_data/death_valley_2021_simple.csv")
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):    # enumerate() returns the index and value of each item in a list
    print(index, column_header)

# Get high temperatures from the file
dates, highs, lows = [], [], []

for row in reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")  # year, month, day

    try:
        high = int(row[3])  # each line is treated as a list with each comma separated value as an element
        low = int(row[4])

    except ValueError:
        print(f"Missing data for {current_date}")

    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

print(f"\nHighest temperatures each day: {highs}")

# Plot the high temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')
ax.plot(dates, lows, color='blue')
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.3)  # alpha controls the transparency of the fill

# Format plot
plt.title("2021 Daily High and Low Temperatures in Death Valley, California", fontsize=15)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()  # draws the date labels diagonally to prevent overlap
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
