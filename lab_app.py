import streamlit as st
import pandas as pd
import numpy as np

# Sidebar navigation (Bonus Task)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Laboratory Activity", "Lesson 1", "Lesson 2", "Lesson 3"])

# Page 1: Laboratory Activity
if page == "Laboratory Activity":
    # 1. Create a title and introduction
    st.title("Streamlit Laboratory Activity")
    st.write("""
    Welcome to this interactive Streamlit application! This app demonstrates the concepts learned 
    from Lessons 1-3, including user input widgets, data display, and CSV visualization.
    """)
    
    st.header("User Information")
    
    # 2. Add input fields for name, age, and favorite subject
    name = st.text_input("Enter your name:", "")
    age = st.number_input("Enter your age:", min_value=0, max_value=120, value=25)
    favorite_subject = st.text_input("Enter your favorite subject:", "")
    
    # 3. Use widgets such as selectbox and radio buttons
    st.subheader("Additional Preferences")
    gender = st.radio("Select your gender:", ["Male", "Female", "Other"])
    education_level = st.selectbox("Select your education level:", 
                                    ["High School", "Bachelor's", "Master's", "Doctorate"])
    hobbies = st.multiselect("Select your hobbies:", 
                              ["Reading", "Sports", "Music", "Coding", "Traveling", "Gaming"])
    
    # 4. Display user input dynamically
    st.header("Your Information Summary")
    if name:
        st.write(f"**Name:** {name}")
        st.write(f"**Age:** {age}")
        st.write(f"**Favorite Subject:** {favorite_subject}")
        st.write(f"**Gender:** {gender}")
        st.write(f"**Education Level:** {education_level}")
        st.write(f"**Hobbies:** {', '.join(hobbies) if hobbies else 'None selected'}")
    else:
        st.info("Please enter your information above to see the summary.")
    
    # 5. Allow user to upload CSV and visualize one selected column
    st.header("CSV Data Visualization")
    uploaded_file = st.file_uploader("Upload a CSV file:", type="csv")
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.write("### Data Preview")
            st.dataframe(df.head())
            
            # Get numeric columns only for visualization
            numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
            
            if numeric_columns:
                selected_column = st.selectbox("Select a column to visualize:", numeric_columns)
                
                st.write(f"### Bar Chart of {selected_column}")
                st.bar_chart(df[selected_column])
            else:
                st.warning("No numeric columns found in the uploaded CSV for visualization.")
        except Exception as e:
            st.error(f"Error reading CSV file: {e}")
    else:
        st.info("Upload a CSV file to see data visualization.")

# Page 2: Lesson 1 Content
elif page == "Lesson 1":
    st.title("Lesson 1: Introduction to Streamlit")
    st.write("""
    Streamlit is an open-source Python framework that lets you create interactive web apps 
    for data and machine learning. It is ideal for dashboards, data visualization, and quick prototypes.
    """)
    
    st.subheader("Installation")
    st.code("pip install streamlit", language="bash")
    
    st.subheader("Run Demo App")
    st.code("streamlit hello", language="bash")
    
    st.subheader("Basic Example")
    basic_code = """import streamlit as st

st.title("Hello Streamlit!")
st.write("This is my first Streamlit app!")
name = st.text_input("Enter your name:")
st.write(f"Hello, {name}!")"""
    st.code(basic_code, language="python")
    
    st.subheader("Try it here:")
    demo_name = st.text_input("Enter your name:")
    if demo_name:
        st.write(f"Hello, {demo_name}!")

# Page 3: Lesson 2 Content
elif page == "Lesson 2":
    st.title("Lesson 2: Streamlit Basics — Layout and Widgets")
    st.write("Streamlit provides easy-to-use display elements and widgets for building interactive web apps.")
    
    st.subheader("Common Display Commands")
    st.write("1. `st.title()`, `st.header()`, `st.subheader()`")
    st.write("2. `st.text()`, `st.write()`, `st.markdown()`")
    st.write("3. `st.image()`, `st.video()`, `st.audio()`")
    
    st.subheader("User Input Widgets")
    st.write("1. `st.button()`, `st.checkbox()`, `st.radio()`")
    st.write("2. `st.selectbox()`, `st.multiselect()`")
    st.write("3. `st.slider()`, `st.text_input()`, `st.number_input()`")
    st.write("4. `st.date_input()`, `st.file_uploader()`")
    
    st.subheader("Example Widget Demo")
    gender_demo = st.radio("Select your gender", ["Male", "Female", "Other"])
    age_demo = st.slider("Select your age", 0, 100, 25)
    st.write(f"Gender: {gender_demo}, Age: {age_demo}")

# Page 4: Lesson 3 Content
elif page == "Lesson 3":
    st.title("Lesson 3: Displaying Data in Streamlit")
    st.write("Streamlit supports data display through tables and visualizations.")
    
    st.subheader("Displaying DataFrames")
    data = {"Name": ["Alice", "Bob", "Charlie"], "Score": [85, 90, 88]}
    df = pd.DataFrame(data)
    st.write("Sample DataFrame:")
    st.dataframe(df.style.highlight_max(axis=0))
    
    st.subheader("Visualizing Data")
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C']
    )
    
    st.write("Line Chart:")
    st.line_chart(chart_data)
    
    st.write("Bar Chart:")
    st.bar_chart(chart_data)
    
    st.subheader("File Upload Example")
    upload_code = """uploaded_file = st.file_uploader("Upload CSV", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df.head())"""
    st.code(upload_code, language="python")

# Footer
st.sidebar.markdown("---")
st.sidebar.info("Streamlit Lab Activity - Lessons 1-3")