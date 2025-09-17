import pandas as pd
import geopandas as gpd
import folium

def create_geospatial_map():
    """Analyzes geospatial data and generates an interactive map."""
    try:
        # Load geospatial data (e.g., NYC Taxi Zones)
        zones = gpd.read_file('data/taxi_zones.shp')
        
        # Load sample data (e.g., aggregated taxi trip counts per zone)
        # For a real project, this data would be from a large CSV or database
        sample_data = pd.DataFrame({
            'LocationID': zones['LocationID'].values,
            'trip_counts': [1000, 2500, 500, 1200, 800, 3000, 1500, 900, 2000, 1800, 
                             2200, 700, 1100, 2800, 600, 1900, 2100, 1400, 2600, 950]
        })

        # Merge the two dataframes
        merged = zones.merge(sample_data, on='LocationID', how='left')

        # Create a base map
        m = folium.Map(location=[40.7128, -74.0060], zoom_start=11)

        # Create a choropleth layer
        folium.Choropleth(
            geo_data=merged,
            name='choropleth',
            data=merged,
            columns=['LocationID', 'trip_counts'],
            key_on='feature.properties.LocationID',
            fill_color='YlGnBu',
            fill_opacity=0.7,
            line_opacity=0.2,
            legend_name='Trip Counts'
        ).add_to(m)

        # Save the map as an HTML file
        m.save('nyc_map.html')
        print("Interactive map saved to nyc_map.html")
        print("Open the file in your browser to view the visualization.")

    except FileNotFoundError:
        print("Error: Required data files were not found.")
        print("Please download the NYC Taxi Zones shapefile and place it in the 'data' directory.")

if __name__ == "__main__":
    create_geospatial_map()
