import folium
import webbrowser

# Dhaka coordinates
dhaka = [23.8103, 90.4125]

m = folium.Map(location=dhaka, zoom_start=12)

folium.Marker(
    dhaka,
    popup="Dhaka, Bangladesh"
).add_to(m)

m.save("dhaka_map.html")

webbrowser.open("dhaka_map.html")