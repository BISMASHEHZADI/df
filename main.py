import streamlit as st
import pandas as pd
# st.title('Hello World')
# st.header('This is a header')
# st.subheader('This is a subheader')
# st.markdown("my name is bisma. I am a student of computer science")

# st.code("""
#         for i in range(1,10):
#             print(i)
#         """)
# # st.text_input('Enter your name')
# # st.text_area('Enter your message')

# dataset = pd.read_csv("h.csv", encoding="latin1", header=None)



# st.dataframe(dataset)
st.title('Student Information')

name = st.text_input('Enter your name')
fname = st.text_input('Enter your father name')
adr = st.text_area('Enter your text')
classdata = st.selectbox('Select your class', ['1st', '2nd', '3rd', '4th', '5th'])
button = st.button('Submit')
if button:
    st.markdown(f"""
                Name: {name}
                Father Name: {fname}    
                Address: {adr}
                Class: {classdata}
                
                """)