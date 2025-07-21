import streamlit as st
import numpy as np
import joblib

# Load Model and label encoder 
model = joblib.load("logistic_model.pkl")
grade_encoder = joblib.load("Grade_encoder.pkl")

st.title("🎓 Student Performance Predictor 🎓")
st.markdown("Enter the Student's Details below")

# User Input
col1, col2, col3 = st.columns(3)
with col1:
    Age = st.number_input("Age", min_value= 15, max_value=40, value= 20)
with col2:
    ApproxHeight = st.number_input("Approximate Height in (CM)")
with col3:
    ApproxWeight = st.number_input("Approximate Weight in (KG)") 
    

col4, col5, col6 = st.columns(3)
with col4: 
    KCSE = st.number_input("KCSE",max_value=2040, min_value=2000, value=2020)
with col5:
    Yr_JoinCampus = st.number_input("Year of joining Campus",max_value=2040, min_value=2000, value=2020)
with col6:
    Expense_Semester = st.number_input("Expence of Semester ",max_value=100000, min_value=20000, value=30000)
    
    
col7,_ =  st.columns([1,2])
with col7:
    Expense_Accommodation = st.number_input("Expence of Accomodation ",max_value=150000, min_value=20000, value=30000) 


# Encoded dropdowm
col8, col9, col10 = st.columns(3)
with col8:
    course = st.selectbox("Course", ['MATHEMATICS', 'ECONOMICS AND STATISTICS', 'URBAN PLANNING', 'ACTUARIAL SCIENCE', 'ECONOMICS', 'STATISTICS', 'APPLIED MATHEMATICS', 'ELECTRICAL ENGINEERING'])
with col9:
    sitkcse = st.selectbox("KCSE Sitting Region", ['Central ', 'Rift Valley' ,'Western', 'Coast', 'Nyanza', 'Nairobi', 'Eastern'])
with col10:
    YearofStudy = st.selectbox("Year of Study", ['First Year', 'Second Year', 'Third Year', 'Fourtth Year'])

course_mapping = {'MATHEMATICS':5,'ECONOMICS AND STATISTICS':3,'URBAN PLANNING':7,'ACTUARIAL SCIENCE':0,'ECONOMICS':2,'STATISTICS':6,'APPLIED MATHEMATICS':1,'ELECTRICAL ENGINEERING':4}
sitkcse_mapping = {'Central ':0, 'Rift Valley':5 ,'Western': 6, 'Coast':1, 'Nyanza':4, 'Nairobi':3, 'Eastern':2}
YearofStudy_mapping = {'First Year': 1, 'Second Year': 2, 'Third Year': 3, 'Fourtth Year': 4}

course_encoded = course_mapping[course]
region_encoded = sitkcse_mapping[sitkcse]
YearofStudy_encoded = YearofStudy_mapping[YearofStudy]


# Predicted Button 
if st.button("Predicted Grade"):
    # Arrange inputs in the same order as training
    features = np.array([[YearofStudy_encoded, Age, ApproxHeight, ApproxWeight, KCSE, Yr_JoinCampus, Expense_Semester,
                          Expense_Accommodation, course_encoded, region_encoded]])
    
    prediction = model.predict(features)
    predicted_grade = grade_encoder.inverse_transform(prediction)[0]
    st.success(f"🎓 STUDENT GRADE SHOULD: **{predicted_grade}**")