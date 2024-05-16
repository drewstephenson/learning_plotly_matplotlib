from pathlib import Path
import json
import plotly.express as px

# Read data as a string and convert to a Python object
path = Path("eq_data/eq_data_30_day_m1.geojson")
contents = path.read_text(encoding='utf-8')
data = json.loads(contents)

# Create an easier to read version of file
path = Path('eq_data/eq_data_1_day_m1_readable.geojson')
path.write_text(json.dumps(data, indent=4))

# Examine all earthquakes in the file
dicts = data['features']

mags, longs, lats, titles = [], [], [], []
for dict in dicts:
    mag = dict['properties']['mag']
    long = dict['geometry']['coordinates'][0]
    lat = dict['geometry']['coordinates'][1]
    title = dict['properties']['title']
    mags.append(mag)
    longs.append(long)
    lats.append(lat)
    titles.append(title)

# Plot the data
title = "Global Earthquakes"
fig = px.scatter_geo(lat=lats, lon=longs, size=mags, title=title,
                     color=mags,
                     color_continuous_scale='Viridis',
                     labels={'color': 'Magnitude'},
                     projection='natural earth',
                     hover_name=titles,
                     )
fig.show()

print(mags)
print(longs)
print(lats)
