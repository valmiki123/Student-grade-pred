import streamlit as st
import pickle

model=pickle.load(open('modle.pkl','rb'))

st.title('Student Grade Prediction System')
g1=st.number_input('Enter Grades for Mid1')
g2=st.number_input('Enter Grades for Mid2')
studytime=st.number_input('Enter duration of study hours')
failures=st.number_input('Enter number of failed exams')
absences=st.number_input('Enter number of absent classes')

if st.button('Predict'):
    data=[[g1,g2,studytime,failures,absences]]
    out=model.predict(data)
    if(out[0]>20):
        out[0]=20
    st.success(out[0])
