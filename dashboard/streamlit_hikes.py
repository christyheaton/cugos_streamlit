import streamlit as st
import pandas as pd
import altair as alt


def main():
    st.title("Washington Hikes")
    hikes_df = pd.read_csv("../data/2021-04-25_wta_hike_data_clean.csv")

    st.subheader("Filters")

    min_dist = int(hikes_df["DISTANCE"].min())
    max_dist = 30
    dist_slider = st.slider("Distance:", min_dist, max_dist, (min_dist, max_dist))

    min_elev = int(hikes_df["GAIN"].min())
    max_elev = 4500
    elev_slider = st.slider("Elevation Gain:", min_elev, max_elev, (min_elev, max_elev))

    region = st.selectbox("Region:", ["All"] + hikes_df["REGION"].tolist())

    # Filtered data
    filtered_df = hikes_df[(hikes_df["DISTANCE"] >= dist_slider[0]) &
                           (hikes_df["DISTANCE"] <= dist_slider[1]) &
                           (hikes_df["GAIN"] >= elev_slider[0]) &
                           (hikes_df["GAIN"] <= elev_slider[1])]
    if region != "All":
        filtered_df = filtered_df[(filtered_df["REGION"] == region)]

    st.subheader("Hike Table")
    st.dataframe(filtered_df)

    st.subheader("Hike Map")
    st.map(data=filtered_df,
           latitude="Latitude",
           longitude="Longitude")

    # Hike ratings chart
    filtered_df["rounded_rating"] = filtered_df["RATING"].round()
    rating_counts = filtered_df["rounded_rating"].value_counts().reset_index()
    rating_counts.columns = ["rating", "count"]

    st.subheader("Hike Ratings")

    bar_chart = alt.Chart(rating_counts).mark_bar(color="skyblue").encode(
        x=alt.X("rating:O", title="Rating"),
        y=alt.Y("count:Q", title="Count")
    )
    st.altair_chart(bar_chart, use_container_width=True)
    average_rating = filtered_df['RATING'].mean()
    st.text(f"Average rating: {average_rating}")

    # Random hike selector
    if not filtered_df.empty:
        if st.button("Select Random Hike"):
            random_row = filtered_df.sample()
            st.subheader("Randomly Selected Hike")
            st.table(random_row.T)
            st.map(data=random_row,
                   latitude="Latitude",
                   longitude="Longitude")

    # Highest rated hike selector
    if not filtered_df.empty:
        if st.button("Select Highest Rated Hike"):
            highest = filtered_df.loc[filtered_df["RATING"].idxmax()].to_frame().T
            st.subheader("Highest Rated Hike")
            st.table(highest.T)
            st.map(data=highest,
                   latitude="Latitude",
                   longitude="Longitude")


if __name__ == "__main__":
    main()
