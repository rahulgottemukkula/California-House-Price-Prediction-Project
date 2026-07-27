import streamlit as st
import pickle
import pandas as pd

# Load model and preprocessors
model = pickle.load(open("california_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
encoder = pickle.load(open("encoder.pkl", "rb"))

st.set_page_config(page_title="California House Price Prediction")

st.title("🏡 California House Price Prediction")

# ==========================
# User Inputs
# ==========================

longitude = st.number_input("Longitude", value=-122.23)
latitude = st.number_input("Latitude", value=37.88)
housing_median_age = st.number_input("Housing Median Age", value=41)

total_rooms = st.number_input("Total Rooms", min_value=1, value=880)
total_bedrooms = st.number_input("Total Bedrooms", min_value=1, value=129)

population = st.number_input("Population", min_value=1, value=322)
households = st.number_input("Households", min_value=1, value=126)

median_income = st.number_input("Median Income", value=8.3252)

ocean = st.selectbox(
    "Ocean Proximity",
    [
        "<1H OCEAN",
        "INLAND",
        "ISLAND",
        "NEAR BAY",
        "NEAR OCEAN"
    ]
)

# ==========================
# Predict Button
# ==========================

if st.button("Predict House Price"):

    # Feature Engineering
    rooms_per_household = total_rooms / households
    bedrooms_per_room = total_bedrooms / total_rooms
    population_per_household = population / households

    # Numerical dataframe
    num_data = pd.DataFrame([[
        longitude,
        latitude,
        housing_median_age,
        total_rooms,
        total_bedrooms,
        population,
        households,
        median_income,
        rooms_per_household,
        bedrooms_per_room,
        population_per_household
    ]],
    columns=[
        "longitude",
        "latitude",
        "housing_median_age",
        "total_rooms",
        "total_bedrooms",
        "population",
        "households",
        "median_income",
        "rooms_per_household",
        "bedrooms_per_room",
        "population_per_household"
    ])

    # Scale numerical features
    num_scaled = scaler.transform(num_data)

    final_input = pd.DataFrame(
        num_scaled,
        columns=num_data.columns
    )

    # Encode categorical feature
    final_input["ocean_proximity"] = encoder.transform([ocean])[0]

    # Prediction
    prediction = model.predict(final_input)

    st.success(f"🏠 Predicted House Price: ${prediction[0]:,.2f}")