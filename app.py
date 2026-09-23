import streamlit as st
import pickle
import pandas as pd

model=pickle.load(open(r'C:\Users\tejas\Downloads\Salary prediction\linear regression.pkl','rb'))
df = pd.read_csv(r'C:\Users\tejas\Downloads\Salary prediction\salary_prediction_ml_dataset.csv')




st.title(" Employee Salary Prediction")

st.write(
    "Enter the employee details below to predict the expected salary."
)

st.divider()


st.header(" Employee Details")



col1, col2, col3, col4 = st.columns(4)

with col1:
    age = st.number_input("Age",min_value=21,max_value=60)

with col2:
    years_experience = st.number_input("Years Experience",min_value=0,max_value=40)

with col3:
    education_level = st.selectbox("Education_Level",df['Education_Level'].unique())

with col4:
    job_level = st.selectbox("Job Level",df["Job_Level"].unique())


col1, col2, col3, col4 = st.columns(4)

with col1:
    department = st.selectbox("Department",df["Department"].unique())

with col2:
    employment_type = st.selectbox("Employment Type",df['Employment_Type'].unique())

with col3:
    performance_rating = st.slider("Performance Rating",min_value=1,max_value=5,value=3)

with col4:
    company_size = st.selectbox("Company Size",df["Company_Size"].unique())

col1, col2, col3, col4 = st.columns(4)

with col1:
    training_hours = st.number_input("Training Hours",min_value=0,max_value=100,value=20)

with col2:
    projects_completed = st.number_input("Projects Completed",min_value=0,max_value=100,value=5)

with col3:
    certifications = st.number_input("Certifications",min_value=0,max_value=20,value=2)

with col4:
    weekly_work_hours = st.number_input("Weekly Work Hours",min_value=20,max_value=100,value=40)


col1, col2, col3, col4 = st.columns(4)

with col1:
    job_satisfaction = st.slider("Job Satisfaction",min_value=1,max_value=5,value=3)

with col2:
    career_stage = st.slider("Career Stage",min_value=0,max_value=10)

with col3:
    has_degree = st.selectbox("Has Degree",df['Has_Degree'].unique())

with col4:
    leadership_role = st.selectbox("Leadership Role",df['Leadership_Role'].unique())



col1, col2, col3, col4 = st.columns(4)

with col1:
    international_experience = st.selectbox("International Experience",df['International_Experience'].unique())


st.divider()

predict = st.button("Predict Salary",type="primary")

if predict:

    input_data = pd.DataFrame({
        "Age": [age],
        "Years_Experience": [years_experience],
        "Education_Level": [education_level],
        "Job_Level": [job_level],
        "Department": [department],
        "Employment_Type": [employment_type],
        "Performance_Rating": [performance_rating],
        "Company_Size": [company_size],
        "Training_Hours": [training_hours],
        "Projects_Completed": [projects_completed],
        "Certifications": [certifications],
        "Weekly_Work_Hours": [weekly_work_hours],
        "Job_Satisfaction": [job_satisfaction],
        "Career_Stage": [career_stage],
        "Has_Degree": [has_degree],
        "Leadership_Role": [leadership_role],
        "International_Experience": [international_experience]
    })

    prediction = model.predict(input_data)

    salary = prediction[0]


    st.success("Salary Prediction Completed!")

    st.subheader(" Predicted Salary")

    st.metric(label="Annual Salary",value=f"₹ {salary:,.2f}")


