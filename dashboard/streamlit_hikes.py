import streamlit as st
import pandas as pd
import altair as alt


def main():
    hikes_df = pd.read_csv("../data/2021-04-25_wta_hike_data_clean.csv")
    st.title("Washington Hikes")

    st.subheader("Filters")

    min_dist = int(hikes_df["DISTANCE"].min())
    dist_slider = st.slider("Distance:", min_dist, 30, (min_dist, 30))

    min_elev = int(hikes_df["GAIN"].min())
    elev_slider = st.slider("Elevation Gain:", min_elev, 4500, (min_elev, 4500))

    region = st.selectbox("Region:", ["All"] + hikes_df["REGION"].tolist())

    # Filtered data
    if region == "All":
        filtered_df = hikes_df[(hikes_df["DISTANCE"] >= dist_slider[0]) &
                               (hikes_df["DISTANCE"] <= dist_slider[1]) &
                               (hikes_df["GAIN"] >= elev_slider[0]) &
                               (hikes_df["GAIN"] <= elev_slider[1])]

    else:
        filtered_df = hikes_df[(hikes_df["REGION"] == region) &
                               (hikes_df["DISTANCE"] >= dist_slider[0]) &
                               (hikes_df["DISTANCE"] <= dist_slider[1]) &
                               (hikes_df["GAIN"] >= elev_slider[0]) &
                               (hikes_df["GAIN"] <= elev_slider[1])]

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
    rating_counts["rating"] = rating_counts["rating"].astype(int)

    st.subheader("Hike Ratings")

    bar_chart = alt.Chart(rating_counts).mark_bar(color="skyblue").encode(
        x=alt.X("rating:O", title="Rating"),
        y=alt.Y("count:Q", title="Count")
    )
    st.altair_chart(bar_chart, use_container_width=True)
    average_rating = filtered_df['RATING'].mean()
    st.text(f"Average rating: {average_rating}")

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
