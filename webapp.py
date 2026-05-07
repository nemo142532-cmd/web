import streamlit as st
import pickle
import numpy as np

LR=pickle.load(open('classifier.pkl','rd'))
DT=pickle.load(open('base_model2.pkl','rb'))
RF=pickle.load(open('rf.pkl','rd'))

st.set_page_config(
    page_title="Shopping Prediction",
    page_icon="🛒",
    layout="centered")

st.title("🛒 Online Shopping Prediction App")
st.write("Enter user details to predict if they will complete purchase")

st.divider()

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=0)
    gender = st.selectbox("Gender", [0, 1])
    frequency = st.number_input("Shopping Frequency")

    browsing = st.number_input("Browsing Time")

    reviews = st.selectbox("Reads Reviews", [0, 1])

with col2:
    device = st.selectbox("Device", [0, 1])
    compare = st.selectbox("Compare Prices", [0, 1])
    discount = st.selectbox("Discount Influence", [0, 1, 2])
    cart = st.selectbox("Abandoned Cart", [0, 1])
    factor = st.selectbox("Important Factor", [0, 1, 2])

st.divider()

if st.button("Predict", use_container_width=True):

    input_data = np.array([[age, gender, frequency, device,
                            browsing, reviews, compare,
                            discount, cart, factor]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("User WILL complete purchase")
        st.balloons()
    else:
        st.error("User will NOT complete purchase")