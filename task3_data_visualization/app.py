import pandas as pd
import streamlit as st
import plotly.express as px

# Page configuration
st.set_page_config(page_title="Job Analytics Dashboard", layout="wide", page_icon="📊")
st.title("📊 Job Market Analytics Dashboard")
st.markdown("Interactive exploration of scraped job listings data.")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("scraped_job_data.csv")
    df["Date Posted"] = pd.to_datetime(df["Date Posted"], errors="coerce")
    return df

try:
    df = load_data()

    # Sidebar Controls
    st.sidebar.header("🔍 Filter Options")
    
    # Filter 1: Search by Job Title keyword
    search_keyword = st.sidebar.text_input("Search Job Title:", placeholder="e.g. Developer, Engineer")
    
    # Filter 2: Select Companies
    all_companies = sorted(df["Company"].dropna().unique().tolist())
    selected_companies = st.sidebar.multiselect(
        "Select Companies:",
        options=all_companies,
        default=[],
        help="Leave empty to select all companies"
    )

    # Filter 3: Select Locations
    all_locations = sorted(df["Location"].dropna().unique().tolist())
    selected_locations = st.sidebar.multiselect(
        "Select Locations:",
        options=all_locations,
        default=[],
        help="Leave empty to select all locations"
    )

    # Apply Filters Dynamically
    filtered_df = df.copy()
    
    if search_keyword:
        filtered_df = filtered_df[filtered_df["Job Title"].str.contains(search_keyword, case=False, na=False)]
        
    if selected_companies:
        filtered_df = filtered_df[filtered_df["Company"].isin(selected_companies)]
        
    if selected_locations:
        filtered_df = filtered_df[filtered_df["Location"].isin(selected_locations)]

    # Key Performance Indicators (KPIs)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Matching Openings", len(filtered_df))
    col2.metric("Filtered Companies", filtered_df["Company"].nunique())
    col3.metric("Filtered Locations", filtered_df["Location"].nunique())
    col4.metric("Total Database Records", len(df))

    st.divider()

    # Interactive Plotly Charts (Supports Zoom, Hover, Pan)
    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        st.subheader("Top Hiring Companies")
        top_comp = filtered_df["Company"].value_counts().head(10).reset_index()
        top_comp.columns = ["Company", "Count"]
        if not top_comp.empty:
            fig1 = px.bar(
                top_comp, x="Count", y="Company", orientation='h',
                color="Count", color_continuous_scale="Blues",
                labels={"Count": "Openings", "Company": "Company Name"}
            )
            fig1.update_layout(yaxis={'categoryorder':'total ascending'}, showlegend=False, height=400)
            st.plotly_chart(fig1, use_container_width=True)
        else:
            st.info("No companies match the current filter selection.")

    with chart_col2:
        st.subheader("Top Job Locations")
        top_loc = filtered_df["Location"].value_counts().head(10).reset_index()
        top_loc.columns = ["Location", "Count"]
        if not top_loc.empty:
            fig2 = px.bar(
                top_loc, x="Count", y="Location", orientation='h',
                color="Count", color_continuous_scale="Viridis",
                labels={"Count": "Openings", "Location": "Location Name"}
            )
            fig2.update_layout(yaxis={'categoryorder':'total ascending'}, showlegend=False, height=400)
            st.plotly_chart(fig2, use_container_width=True)
        else:
            st.info("No locations match the current filter selection.")

    st.divider()

    # Interactive Data Table with CSV Export
    st.subheader("📋 Interactive Dataset View")
    st.dataframe(filtered_df, use_container_width=True, height=300)

    # Download Filtered Data Button
    csv_data = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Filtered Data as CSV",
        data=csv_data,
        file_name="filtered_job_data.csv",
        mime="text/csv",
    )

except Exception as e:
    st.error(f"Error: {e}. Please check if 'scraped_job_data.csv' is in the project folder.")
