# app.py
import streamlit as st
import pickle
import numpy as np
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

# -----------------------
# Page configuration
# -----------------------
st.set_page_config(
    page_title="Boston Housing Predictor",
    page_icon="🏠",
    layout="centered"
)

# -----------------------
# Load the trained model
# -----------------------
@st.cache_resource
def load_model():
    model_path = "E:/Boston-Housing-ML/Boston-Housing-ML/model/model.pkl"
    
    # Check if model exists
    if not os.path.exists(model_path):
        st.error(f"❌ Model not found at: {model_path}")
        st.info("Please make sure the model file exists at the specified path.")
        return None
    
    try:
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        return model
    except Exception as e:
        st.error(f"❌ Error loading model: {e}")
        return None

# Load model
model = load_model()

# -----------------------
# App Header
# -----------------------
st.title("🏠 Boston Housing Price Predictor")
st.markdown("---")

if model is None:
    st.stop()

# -----------------------
# Main content
# -----------------------
st.write("""
### Enter the house features below:
Fill in the values to get an instant price prediction.
""")

# Create three columns for better layout
col1, col2, col3 = st.columns(3)

with col1:
    rooms = st.number_input(
        "🛏️ **Rooms (RM)**", 
        min_value=3, 
        max_value=9, 
        value=6,
        step=1,
        help="Average number of rooms per dwelling (typical range: 3-9)"
    )

with col2:
    poverty = st.number_input(
        "📉 **Poverty % (LSTAT)**", 
        min_value=1, 
        max_value=40, 
        value=12,
        step=1,
        help="Percentage of lower status population (typical range: 1-40%)"
    )

with col3:
    ptratio = st.number_input(
        "👨‍🏫 **Pupil-Teacher Ratio**", 
        min_value=12, 
        max_value=22, 
        value=15,
        step=1,
        help="Student to teacher ratio (typical range: 12-22)"
    )

# Add some visual spacing
st.markdown("---")

# -----------------------
# Prediction button and result
# -----------------------
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    predict_button = st.button("🔮 Predict Price", use_container_width=True, type="primary")

if predict_button:
    # Prepare features for prediction
    client_features = np.array([[rooms, poverty, ptratio]])
    
    # Make prediction
    try:
        predicted_price = model.predict(client_features)[0]
        
        # Display result in a nice box
        st.markdown("### 📊 Prediction Result")
        
        # Create a metrics row
        metric_col1, metric_col2, metric_col3 = st.columns(3)
        
        with metric_col1:
            st.metric("Rooms", f"{rooms:.1f}")
        
        with metric_col2:
            st.metric("Poverty Level", f"{poverty:.1f}%")
        
        with metric_col3:
            st.metric("P/T Ratio", f"{ptratio:.1f}")
        
        # Main price display
        st.markdown(f"""
        <div style="
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            margin: 20px 0;
        ">
            <h2 style="color: #1f77b4; margin: 0;">💰 ${predicted_price:,.2f}</h2>
            <p style="color: #666; margin: 5px 0 0 0;">Predicted Selling Price</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Provide context for the prediction
        if predicted_price < 15000:
            st.warning("⚠️ This price is in the lower range. The house might need renovations or be in a less desirable area.")
        elif predicted_price > 35000:
            st.success("✨ This price is in the upper range. The house likely has many rooms and is in a good neighborhood.")
        else:
            st.info("📊 This price is in the average range for the Boston area.")
            
    except Exception as e:
        st.error(f"❌ Prediction error: {e}")

# -----------------------
# Footer
# -----------------------
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666;'>
        <p>Built with ❤️ using Streamlit | Boston Housing Dataset</p>
    </div>
    """, 
    unsafe_allow_html=True
)