# Geospatial Data Analysis & Visualization

## Project Overview

This project focuses on the analysis and visualization of geospatial data to identify and understand urban trends. The core of the project involves using Python libraries to process geographical data, perform spatial analysis, and generate an interactive map that reveals patterns and insights.

This project is a great way to showcase skills in data analysis, visualization, and solving real-world problems using a dataset that goes beyond a standard spreadsheet.

## Key Features

-   **Geospatial Data Processing:** Reads and manipulates shapefile or GeoJSON data using GeoPandas.
-   **Spatial Analysis:** Performs a spatial join to link data points to specific geographical areas.
-   **Interactive Visualization:** Creates a beautiful, interactive choropleth map using Folium, saved as an HTML file.

## Technologies Used

-   **Python**
-   **Libraries:** pandas, geopandas, folium

## Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/geospatial-analysis.git](https://github.com/your-username/geospatial-analysis.git)
    cd geospatial-analysis
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Download your data:**
    * For this project, you will need a geospatial dataset. A great, beginner-friendly option is the **NYC Taxi Zones shapefile** and **taxi trip data**.
    * Place your shapefiles (e.g., `taxi_zones.shp`) and CSV data (e.g., `taxi_data.csv`) in a `data/` subdirectory.

5.  **Run the script:**
    ```bash
    python geospatial_analysis.py
    ```
    This will generate a file named `nyc_map.html` in your project directory. Open it in your web browser to view the interactive map.

## Data Source

This project can use various open data sources. A great starting point is the **NYC Open Data Portal**, specifically the taxi trip records and taxi zones shapefile.
