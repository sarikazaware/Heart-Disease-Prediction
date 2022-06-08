import streamlit as st
import numpy as np
import pickle as pkl
model1 = pkl.load(open("model.pkl","rb"))

st.set_page_config(page_title="Heart Disease Predication", initial_sidebar_state="expanded", layout="wide")

def preprocess(BMI,Smoking,AlcoholDrinking,Stroke,PhysicalHealth,MentalHealth,DiffWalking,Sex,AgeCategory,Race,Diabetic,PhysicalActivity,Asthma,KidneyDisease,SkinCancer):
    if Smoking=="Yes":
        Smoking=1
    else:
        Smoking=0
        
    if AlcoholDrinking=="Yes":
        AlcoholDrinking=1
    else:
        AlcoholDrinking=0
        
    if Stroke=="Yes":
        Stroke=1
    else:
        Stroke=0
        
    if DiffWalking=="Yes":
         DiffWalking=1
    else:
         DiffWalking=0
         
    if Sex=="Male":
        Sex=1 
    else:
        Sex=0
    
    if PhysicalActivity=="Yes":
        PhysicalActivity=1
    else:
        PhysicalActivity=0
        
    if Asthma=="Yes":
        Asthma=1
    else:
        Asthma=0
        
    if KidneyDisease=="Yes":
       KidneyDisease=1
    else:
       KidneyDisease=0     
       
    if SkinCancer=="Yes":
        SkinCancer=1
    else:
        SkinCancer=0     
    
    if AgeCategory=="18-24":
        AgeCategory=0
    elif AgeCategory=="25-29":
        AgeCategory=1
    elif AgeCategory=="30-34":
        AgeCategory=2
    elif AgeCategory=="35-39":
        AgeCategory=3
    elif AgeCategory=="40-44":
        AgeCategory=4
    elif AgeCategory=="45-49":
        AgeCategory=5
    elif AgeCategory=="50-54":
        AgeCategory=6
    elif AgeCategory=="55-59":
        AgeCategory=7
    elif AgeCategory=="65-69":
        AgeCategory=9
    elif AgeCategory=="60-64":
        AgeCategory= 8
    elif AgeCategory=="70-74":
        AgeCategory=10
    elif AgeCategory=="75-79":
        AgeCategory=11
    else:
        AgeCategory=12
        
    if Race=="American Indian":
        Race=0
    elif Race=="Asian":
        Race=1
    elif Race=="Black":
        Race=2
    elif Race=="Hispanic":
        Race=3
    elif Race=="Other":
        Race=4
    else:
        Race=5
    
    if Diabetic=="No":
        Diabetic=0
    elif Diabetic=="No, borderline diabetic":
        Diabetic = 1
    elif Diabetic=="Yes":
        Diabetic = 2
    else:
        Diabetic=3
    
    
    user_input = [BMI,Smoking,AlcoholDrinking,Stroke,PhysicalHealth,MentalHealth,DiffWalking,Sex,AgeCategory,Race,Diabetic,PhysicalActivity,Asthma,KidneyDisease,SkinCancer]
    user_input = np.array(user_input)
    user_input = user_input.reshape(1,-1)
    prediction1 = model1.predict(user_input)

    return prediction1

# front end elements of the web page 
html_temp = """ 
    <div style ="background-color:#D3E6E9; padding:13px"> 
    <h2 style ="color:black; text-align:center; font-family: calibri">Heart Disease Prediction </h2> 
    </div> 
    """
st.markdown(html_temp, unsafe_allow_html = True) 

# Image
col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')

with col2:
    st.image("img.png", width=500)

with col3:
    st.write(' ')

# User input name
name = st.text_input("NAME")

st.subheader('Please fill the following form:')

# Feature input from the users
col1, col2, col3 = st.columns((1,1,2))
with col1:
    BMI = st.number_input("BMI",0, 100)
    PhysicalHealth = st.number_input("Physical Health",0 , 30)
    MentalHealth = st.number_input("Mental Health",0, 30)
    Sex = st.radio('Sex',["Male","Female"])
    Smoking = st.radio('Do you smoke?',["Yes","No"])
    SkinCancer = st.radio('Do you have Skin Cancer?',["Yes","No"])

with col2:
    AlcoholDrinking = st.radio('Do you consume alcohol?',["Yes","No"])
    Stroke = st.radio('Any stroke history?',["Yes","No"])
    DiffWalking = st.radio('Do you have difficulty in walking?',["Yes","No"])
    PhysicalActivity = st.radio('Are you physical activity?',["Yes","No"])
    Asthma = st.radio('Do you have asthama? ',["Yes","No"])
    KidneyDisease = st.radio('Do you have kidney disease?',["Yes","No"])

with col3:
    Race = st.radio("Race",["White","Black", "American Indian", "Asian", "Other", "Hispanic"])
    Diabetic = st.radio ("Specify your diabetis category?",["Yes", "No", "No, borderline", "Yes, during pregnancy"])
    AgeCategory = st.radio ("Select you age",["18-24", "25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79", "80 and above"])


#user_input=preprocess
pred = preprocess(BMI,Smoking,AlcoholDrinking,Stroke,PhysicalHealth,MentalHealth,DiffWalking,Sex,AgeCategory,Race,Diabetic,PhysicalActivity,Asthma,KidneyDisease,SkinCancer)

if st.button("Predict"):    
  if pred[0] == 0:
    st.write(name, ' you high risk of getting heart attack. Please do exercise.')
    
  else:
      st.write(name, "Congratulations!! You have low risk of getting a heart attack")
