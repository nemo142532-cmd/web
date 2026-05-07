import streamlit as st
import pickle
import numpy as np

RF=pickle.load(open('rf.pkl','rb'))

st.set_page_config(
    page_title="Shopping Prediction",
    layout="centered")

st.title("Online Shopping Prediction App")
st.write("Enter user details to predict if they will complete purchase")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Age")
    st.caption("1 = <18 | 2 = 18–24 | 3 = 25–34 | 4 = 35–44")
    age = st.selectbox(" What is your age group?", [1,2,3,4])


    st.subheader("Gender")
    st.caption("1 = Male | 2 = Female")
    gender = st.selectbox(" What is your gender?", [1,2])



    st.subheader("Shopping Frequency")
    st.caption("1 = Rarely | 2 = 1–2 times | 3 = 3–5+ times | 4 = More than 5 time")
    frequency = st.selectbox("How often do you shop online per month?", [1,2,3,4])

    st.subheader("Browsing Time")
    st.caption("1 = <10 min | 2 = 10–30 | 3 = 30+")
    browsing = st.selectbox("How much time do you usually spend browsing before making a purchase?", [1,2,3])


    st.subheader("Reads Reviews")
    st.caption(" 1= Always| 2 = Sometimes | 3 = Rarely  | 4 = Never ")
    reviews = st.selectbox("Do you read product reviews before purchasing?", [1,2,3,4])

with col2:
    
    st.subheader("Device")
    st.caption("1 = Mobile | 2 = Laptop | 3 = Tablet")
    device = st.selectbox("What device do you usually use for online shopping?", [1,2,3])

    st.subheader("Compare Prices")
    st.caption(" 1= Always| 2 = Sometimes | 3 = Rarely  | 4 = Never ")
    compare = st.selectbox("Do you compare prices across different websites?", [1,2,3,4])

    st.subheader("Discount Influence")
    st.caption("1 = A lot | 2 = Somewhat | 3 = A little | 4 = Not at all")
    discount = st.selectbox("Do discounts and offers influence your purchasing decisions?", [1,2,3,4])

    st.subheader("Abandoned Cart")
    st.caption("1 = Yes | 2 = No")
    cart = st.selectbox("Have you ever added items to your cart but did not complete the purchase?", [1,2])

    st.subheader("Important Factor")
    st.caption("1 = Price | 2 = Quality | 3 = Reviews | 4 = Delivery speed | 5 = Brand")
    factor = st.selectbox("What is the most important factor influencing your purchase decision?", [1,2,3,4,5])
    
    
    st.subheader("complete your purchase after browsing products")
    st.caption("1 = Yes | 2 = No ")
    purchase = st.selectbox("Do you usually complete your purchase after browsing products?", [1,2])

st.divider()

if st.button("Predict", use_container_width=True):

    input_data = np.array([[age, gender, frequency, device,
                            browsing, reviews, compare,
                            discount, cart, factor,purchase]])

    prediction = RF.predict(input_data)

    if prediction[0] == 1:
        st.success("User WILL complete purchase")
        st.balloons()
    else:
        st.error("User will NOT complete purchase")
