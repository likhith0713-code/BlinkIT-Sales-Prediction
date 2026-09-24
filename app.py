import streamlit as st
import pandas as pd
import joblib

# Page configuration
st.set_page_config(page_title="Blinkit Sales Intelligence Engine", page_icon="🛒", layout="wide")

st.title("🛒 Blinkit Sales Intelligence Engine")
st.markdown("---")

# Sidebar Input Controls (matching your screenshot layout)
st.sidebar.header("Input Controls")

# Input variables
item_category = st.sidebar.selectbox("Item Category", ['Food', 'Drinks', 'Non-Consumable'])
item_weight = st.sidebar.slider("Item Weight", 4.0, 22.0, 12.5)
item_fat_content = st.sidebar.selectbox("Item Fat Content", ['Low Fat', 'Regular', 'Non-Edible'])
item_visibility = st.sidebar.slider("Item Visibility", 0.001, 0.35, 0.06)
item_type = st.sidebar.selectbox("Item Type", ["Baking Goods", "Breads", "Breakfast", "Canned", "Dairy", "Frozen Foods", "Fruits and Vegetables", "Hard Drinks", "Health and Hygiene", "Household", "Meat", "Others", "Seafood", "Snack Foods", "Soft Drinks", "Starchy Foods"])
item_mrp = st.sidebar.slider("Item MRP", 30.0, 270.0, 140.0)
st.sidebar.caption("ℹ️ Item MRP is displayed for reference only and is not used by the prediction model (not present in the training data).")

outlet_establishment_year = st.sidebar.selectbox("Outlet Establishment Year", [1985, 1987, 1997, 1998, 1999, 2002, 2004, 2007, 2009])
outlet_size = st.sidebar.selectbox("Outlet Size", ['Small', 'Medium', 'High'])
outlet_location_tier = st.sidebar.selectbox("Outlet Location Tier", ['Tier 1', 'Tier 2', 'Tier 3'])
outlet_type = st.sidebar.selectbox("Outlet Type", ['Grocery Store', 'Supermarket Type1', 'Supermarket Type2', 'Supermarket Type3'])

# Main area split into two columns matching your screenshot design
col1, col2 = st.columns([2, 1], gap="medium")

with col1:
    st.subheader("Parsed Input DataFrame")
    
    # Calculate derived features as required by the model
    outlet_age = 2026 - outlet_establishment_year
    rating = 4.0 # Dummy rating since not provided in inputs
    outlet_identifier = "OUT027" # Dummy default, typically a high volume outlet
    
    input_dict = {
        "Item Weight": [item_weight],
        "Item Visibility": [item_visibility],
        "Outlet_Age": [outlet_age],
        "Rating": [rating],
        "Item Fat Content": [item_fat_content],
        "Item Type": [item_type],
        "Item_Category": [item_category],
        "Outlet Identifier": [outlet_identifier],
        "Outlet Location Type": [outlet_location_tier],
        "Outlet Size": [outlet_size],
        "Outlet Type": [outlet_type]
    }
    
    input_df = pd.DataFrame(input_dict)
    
    # Show Item MRP as user selected it, alongside the model inputs table
    display_df = input_df.copy()
    display_df["Item MRP"] = [item_mrp]
    st.dataframe(display_df, use_container_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("🚀 Predict Expected Sales"):
        try:
            model = joblib.load('models/best_model.pkl')
            prediction = model.predict(input_df)
            st.success(f"### Predicted Item Outlet Sales: ₹{prediction[0]:,.2f}")
        except FileNotFoundError:
            st.error("Model file 'models/best_model.pkl' not found. Please train the model first.")
        except Exception as e:
            st.error(f"Error making prediction: {e}")

with col2:
    st.subheader("Retail Strategy Insights")
    st.info("**Outlet Type Influence:** Supermarket Type 3 historically drives the highest sales volume due to greater floor space and foot traffic. Adjust your outlet type to see potential maximum revenue.")
    st.info("**Item MRP Impact:** Higher Item MRP generally correlates with higher expected sales revenue, assuming consistent demand. Adjusting the MRP allows predicting price elasticity effects in retail settings.")

# --- Footer Credits ---
st.markdown("---")
st.markdown("<div style='text-align: center; color: gray;'>Developed by <b>M Y Likhith</b> | IBM SkillsBuild / AICTE Internship Project</div>", unsafe_allow_html=True)