import folium
import pandas

df = pandas.read_csv('Volcanoes_USA.txt')

# Average Latitude and Longitutde to get map center
lat_mean = df['LAT'].mean()
lon_mean = df['LON'].mean()

# Location of map center
location = [lat_mean, lon_mean]

# Create map object for map center
map = folium.Map(location, zoom_start=6, tiles='Stamen Terrain')

def marker_color(elev):

    min_elev = int(min(df['ELEV']))
    step = int((max(df['ELEV'] - min_elev)) / 3)

    if elev in range(min_elev, min_elev + step):
        color = 'orange'
    elif elev in range(min_elev, min_elev + step*2):
        color = 'red'
    else:
        color = 'darkred'

    return color

# Create feature group object for LayerControl
# Can group toggle markers on the map
fg = folium.FeatureGroup(name='Volcano Locations')

# Loop through input data to generate markers
for lat,lon,name,elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):

        folium.Marker(
        location=[lat, lon],
        popup='<b>' + name + '</b>',
        icon=folium.Icon(color=marker_color(elev))
        ).add_to(fg)

map.add_child(fg)

# LayerControl panel
folium.LayerControl().add_to(map)

map.save('test.html')
