import streamlit as st
import pickle

# load the trained model
def load():
    with open('D:\\Projects_hub\\heart_deseases\\gbm_model.pcl', 'rb') as fid:
        return pickle.load(fid)

# gender code
def gender_code(gender):
    gdict = {'man': 0, 'woman': 1}

    return gdict[gender]


# interface for input parameters
age = st.slider('Enter your age:', 18, 100)
weight = st.slider('Enter your weight:',
                   40, 120)
height = st.slider('Enter your height:', 150, 200)

ap_hi = st.slider('Enter systolic blood pressure value:', 24, 240)
ap_lo = st.slider('Enter diastolic blood pressure value:', 15, 150)

gender = st.selectbox('Select your gender:', ['man', 'woman'])
cholesterol = st.selectbox('Select your cholesterol level:', [1, 2, 3])
gluc = st.selectbox('Select your glucose level:', [1, 2, 3])

smoke = st.checkbox('Do you smoke?')
alko = st.checkbox('Do you drink alcohol?')
active = st.checkbox('Do you practice aports?')

# preprocessing
bmi = weight / height**2
ap_diff = ap_hi - ap_lo
gender = gender_code(gender)

if ap_lo > ap_hi:
    st.write('WARNING: Diastolic pressure > systolic pressure. Check your data.')

# params to list
params = [age, gender, ap_hi, cholesterol, gluc,
          smoke, alko, active, bmi, ap_diff]

# prediction
model = load()
y_predict = model.predict_proba([params])[:, 1]
st.write(f'Risk of heart diseases: {round(y_predict, 2)}')