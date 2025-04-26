import streamlit as st
import numpy as np
import joblib

model = joblib.load('healthcare_small_model.pkl')

st.title('Personalized Healthcare Risk Prediction')

st.header('Patient Information')

HighBP = st.selectbox('High Blood Pressure?', [0, 1])
BMI = st.number_input('BMI')
Smoker = st.selectbox('Are you a Smoker?', [0, 1])
PhysActivity = st.selectbox('Do you do Physical Activity?', [0, 1])
Age = st.slider('Age', 18, 100)

if st.button('Predict Risk'):

    user_input = np.array([[HighBP, BMI, Smoker, PhysActivity, Age]])

    prediction = model.predict(user_input)

    if prediction[0] == 1:
        st.error('⚠️ High Risk of Chronic Disease Detected!')
        
        st.subheader('✅ Personalized Recommendations:')

        if BMI >= 30:
            st.write('- Consider a weight loss plan (target BMI < 25).')
        if Smoker == 1:
            st.write('- Strongly advised to quit smoking immediately.')
        if PhysActivity == 0:
            st.write('- Start regular physical exercise (e.g., brisk walk 30 mins/day).')
        if HighBP == 1:
            st.write('- Monitor blood pressure regularly and reduce salt intake.')
        if Age >= 45:
            st.write('- Consider more frequent health screenings.')

        st.subheader('📋 Suggested Follow-up Actions:')
        st.write('- Book a doctor appointment for detailed checkup.')
        st.write('- Blood tests: Cholesterol, Blood Sugar, Kidney Function.')
        st.write('- Discuss possible lifestyle intervention programs.')

    else:
        st.success('✅ Low Risk. Keep maintaining a healthy lifestyle!')