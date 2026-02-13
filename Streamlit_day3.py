import streamlit as st
import pandas as pd
import numpy as np
import os

st.set_page_config(
    page_title="My Cool App",
    page_icon="https://scholar.googleusercontent.com/citations?view_op=medium_photo&user=nunNrB0AAAAJ&citpid=5", # Can be a path to a file, a URL, or an emoji "🚀"
)
# Title of the app
st.title("Researcher Profile with Data")

# Collect basic information
name = "Dr. Nathanael Damilare Ojo"
field = "Chemistry"
institution = "University of Johannesburg"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

st.image(
    "https://scholar.googleusercontent.com/citations?view_op=medium_photo&user=nunNrB0AAAAJ&citpid=5",
    caption="(N.D. Ojo)"
)

# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)
    
# 1. Use text_input instead of file_uploader
file_path = st.text_input("Enter the full path to your Publications CSV:", 
                         placeholder="C:\\Users\\NATHANAEL\\Desktop\\CSS2026\Day3\\streamlit_files\\streamlit_files\\Ojo_publications.csv")

# 2. Add logic to verify and load the file
if file_path:
    # Check if the path actually exists to avoid crashing the app
    if os.path.exists("C:\\Users\\NATHANAEL\\Desktop\\CSS2026\Day3\\streamlit_files\\streamlit_files\\Ojo_publications.csv"):
        try:
            # We use pd.read_csv just like before
            publications = pd.read_csv(file_path)
            
            st.success(f"Successfully loaded: {os.path.basename(file_path)}")
            st.dataframe(publications)
            
        except Exception as e:
            st.error(f"Error reading the CSV: {e}")
    else:
        st.warning("The file path provided does not exist. Please check for typos!")
    
 # Load the data
        df = pd.read_csv(file_path)
        st.dataframe(df)

        # --- DOWNLOAD SECTION ---
        st.divider() # Visual break
        
        # 1. Convert DataFrame to CSV (crucial step)
        csv_data = df.to_csv(index=False).encode('utf-8')

        # 2. Create the download button
        st.download_button(
            label="📥 Download Data as CSV",
            data=csv_data,
            file_name='exported_publications.csv',
            mime='text/csv',
        )

    # except Exception as e:
    #     st.error(f"Error: {e}")   
    
    
    
# if uploaded_file:
#     publications = pd.read_csv("C:/Users/NATHANAEL/Desktop/CSS2026/Day3/streamlit_files/streamlit_files/Ojo_publications.csv")
#     st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add STEM Data Section
st.header("Explore STEM Data")

# Generate dummy data
Cancer_data = pd.DataFrame({
    "Experiment": ["Pros_Cancer", "Cerv_Cancer", "Analysis", "Bres_Cancer", "Ov_cancer"],
    "Occurence (Billion)": [4.2, 1.5, 2.9, 3.4, 7.1],
    "Date": pd.date_range(start="2026-02-02", periods=5),
})

Space_data = pd.DataFrame({
    "Celestial Object": ["Mars", "Venus", "Jupiter", "Saturn", "Moon"],
    "Brightness (Magnitude)": [-2.0, -4.6, -1.8, 0.2, -12.7],
    "Observation Date": pd.date_range(start="2024-01-01", periods=5),
})

Climate_data = pd.DataFrame({
    "City": ["Cape Town", "London", "New York", "Tokyo", "Sydney"],
    "Temperature (°C)": [25, 10, -3, 15, 30],
    "Humidity (%)": [65, 70, 55, 80, 50],
    "Recorded Date": pd.date_range(start="2024-01-01", periods=5),
})

# Tabbed view for STEM data
st.subheader("STEM Data Viewer")
data_option = st.selectbox(
    "Choose a dataset to explore", 
    ["Cancer Experiments", "Space Observations", "Climate Data"]
)

if data_option == "Cancer Experiments":
    st.write("### Cancer Experiment Data")
    st.dataframe(Cancer_data)
    # Add widget to filter by Energy levels
    energy_filter = st.slider("Filter by Occurence (Billion)", 0.0, 10.0, (0.0, 10.0))
    filtered_Cancer = Cancer_data[
        Cancer_data["Occurence (Billion)"].between(energy_filter[0], energy_filter[1])
    ]
    st.write(f"Filtered Results for Energy Range {energy_filter}:")
    st.dataframe(filtered_Cancer)

elif data_option == "Space Observations":
    st.write("### Space Observation Data")
    st.dataframe(Space_data)
    # Add widget to filter by Brightness
    brightness_filter = st.slider("Filter by Brightness (Magnitude)", -15.0, 5.0, (-15.0, 5.0))
    filtered_Space = Space_data[
        Space_data["Brightness (Magnitude)"].between(brightness_filter[0], brightness_filter[1])
    ]
    st.write(f"Filtered Results for Brightness Range {brightness_filter}:")
    st.dataframe(filtered_Space)

elif data_option == "Climate Data":
    st.write("### Climate Data")
    st.dataframe(Climate_data)
    # Add widgets to filter by temperature and humidity
    temp_filter = st.slider("Filter by Temperature (°C)", -10.0, 40.0, (-10.0, 40.0))
    humidity_filter = st.slider("Filter by Humidity (%)", 0, 100, (0, 100))
    filtered_Climate = Climate_data[
        Climate_data["Temperature (°C)"].between(temp_filter[0], temp_filter[1]) &
        Climate_data["Humidity (%)"].between(humidity_filter[0], humidity_filter[1])
    ]
    st.write(f"Filtered Results for Temperature {temp_filter} and Humidity {humidity_filter}:")
    st.dataframe(filtered_Climate)

# Add a contact section
st.header("Contact Information")
email = "dammynath@yahoo.com"

st.write(f"You can reach {name} at {email}.")
