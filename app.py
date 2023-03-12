import streamlit as st
import pickle

# load the trained model
def load():
    with open('D:\\Projects_hub\\heart_deseases\\gbm_model.pcl', 'rb') as fid:
        return pickle.load(fid)

# gender code
def gender_code(gender):
    gdict = {'male': 0, 'female': 1}

    return gdict[gender]

# headings
st.header('Check your risk of heart diseases')
st.write('Enter the required information below to receive the forecast.')

# interface for input parameters
col1, col2 = st.columns(2)

with col1:
    st.subheader('General information:')
    gender = st.selectbox('Select your gender:', ['male', 'female'])
    age = st.slider('Enter your age:', 18, 100)
    weight = st.slider('Enter your weight:', 40, 120)
    height = st.slider('Enter your height:', 150, 200)
    smoke = st.checkbox('Do you smoke?')
    alko = st.checkbox('Do you drink alcohol?')
    active = st.checkbox('Do you lead an active lifestyle?')

with col2:
    st.subheader('Medical indicators:')
    ap_hi = st.slider('Enter systolic blood pressure value:', 24, 240)
    ap_lo = st.slider('Enter diastolic blood pressure value:', 15, 150)
    st.write(':red[WARNING: Diastolic pressure must be larger systolic pressure.]')
    cholesterol = st.radio('Select your cholesterol level:', [1, 2, 3])
    gluc = st.radio('Select your glucose level:', [1, 2, 3])


# preprocessing
bmi = weight / height**2
ap_diff = ap_hi - ap_lo
gender = gender_code(gender)

# params to list
params = [age, gender, ap_hi, cholesterol, gluc,
          smoke, alko, active, bmi, ap_diff]

# prediction
model = load()
y_predict = float(model.predict_proba([params])[:, 1])

st.subheader(' ')
st.subheader(f'Risk of heart diseases: {"{:.0%}".format(y_predict)}')
st.write(':red[NOTE: ] Model prediction is advisory in nature. For more accurate diagnosis, please consult a specialist.')
