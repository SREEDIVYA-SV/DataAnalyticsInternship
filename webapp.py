import streamlit as st 
import joblib 
import numpy as np
import matplotlib.pyplot as plt 
from PIL import Image
st.title('Heart Disease Analysis:')
image = Image.open('heart.jpg')
st.image(image)
reload_model = joblib.load('heartdisease_model')
BMI = st.number_input('Insert a BMI value:')
option = st.radio("Any smoking habits?",('Yes','No'))
if(option=='Yes'):
    Smoking=1
else:
    Smoking=0
option = st.radio("Do you drink alcohol?",('Yes','No'))
if(option=='Yes'):
    AlcoholDrinking=1
else:
    AlcoholDrinking=0
option = st.radio("Any strokes u got previously?",('Yes','No'))
if(option=='Yes'):
    Stroke=1
else:
    Stroke=0
PhysicalHealth = st.number_input('Insert a PhysicalHealth value in range of 0 to 30:')
option = st.radio("Difficulty in walking?",('Yes','No'))
if(option=='Yes'):
    DiffWalking=1
else:
    DiffWalking=0
option = st.radio("You do any physical activities?",('No','Yes'))
if(option=='Yes'):
    PhysicalActivity=1
else:
    PhysicalActivity=0
SleepTime = st.number_input('number of hours you sleep:')
option = st.radio("do you have ashtma?",('No','Yes'))
if(option=='Yes'):
    Asthma=1
else:
    Asthma=0
option  = st.radio("do you have kidney disease?",('No','Yes'))
if(option=='Yes'):
    KidneyDisease=1
else:
    KidneyDisease=0
option = st.radio("do you have skinCancer?",('No','Yes'))
if(option=='Yes'):
    SkinCancer=1
else:
    SkinCancer=0
option = st.selectbox('Male or Female?',('Male','Female'))
if(option=="Male"):
    Male=1
    Female=0
else:
    Male=0
    Female=1
option = st.selectbox('Select your Race?',('American Indian/Alaskan Native','Asian','Black','Hispanic','Other','White'))
AmericanIndian_AlaskanNative=0
Asian=0
Black=0
Hispanic=0
Other=0
White=0
if option=='American Indian/Alaskan Native':
    AmericanIndian_AlaskanNative=1
elif option=='Asian':
    Asian=1
elif option=='Black':
    Black=1
elif option=='Hispanic':
    Hispanic=1
elif option=='Other':
    Other=1
else:
    White=1
Excellent=0
Fair=0
Good=0
Poor=0
Verygood=0
option = st.selectbox('General Health:',('Excellent','Fair','Good','Poor','Very good'))
if option=='Excellent':
    Excellent=1
elif option=='Fair':
    Fair=1
elif option=='Good':
    Good=1
elif option=='Poor':
    Poor=1
else:
    Verygood=1
prediction=reload_model.predict([[BMI,Smoking,AlcoholDrinking,Stroke,PhysicalHealth,DiffWalking,PhysicalActivity,SleepTime,Asthma,KidneyDisease,SkinCancer,Female,Male,AmericanIndian_AlaskanNative,Asian,Black,Hispanic,Other,White,Excellent,Fair,Good,Poor,Verygood]])
st.text('Probability of getting heart disease is:')
st.text(prediction)
