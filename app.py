import os
import requests 
import streamlit as st
from dotenv import load_dotenv
from api_url import *
from csv_upload import *


load_dotenv()

# Retrieve values from .env file
openai_api_key = os.getenv("OPENAI_API_KEY")

alpha_key = os.getenv('ALPHA_KEY')



def user_query():
    user_input = st.text_input("Enter youy Query : ")
    chart_type = st.selectbox("Select the chart type", ("Default", "Bar Chart", "Line Chart", "Pie Chart"))
    submit = st.form_submit_button(label = 'Submit')
    return user_input, chart_type, submit

# function for csv file upload 
def file_upload():
    with st.form(key='file_upload'):
        uploaded_file = st.file_uploader("Select a file")
        submit = st.form_submit_button(label='Upload')
        if uploaded_file is not None:
            fname = uploaded_file.name
            print(fname)
            
            user_input, chart_type, status = user_query()
            
            if status :
                generate_graph(uploaded_file, user_input, chart_type)


# function for API URL given 
def api_url(url):
    print("api url : ", api_url)
    if len(url) > 0 :
        r = requests.get(url)
        data_json = r.json()
        
        data_json = json.dumps(data_json)

        with st.form(key="APIURL"): 
            user_input, chart_type, status = user_query()
            generate_llm_answer(status, user_input, data_json, chart_type)




# Frontend 
st.set_page_config(layout='wide')

st.header("Consumer Case Drafting")

input_type = st.selectbox("Choose Input Type", ("None", "API URL", "Upload CSV File"))

# if user selected the API URL option
if input_type == "API URL" :
    with st.form(key='api_url_form'):
        input_url = st.text_input('Enter API URL ..') + "&apikey=" + alpha_key
        submit_button = st.form_submit_button(label='Submit')
    try:
        api_url(input_url)
    except Exception as e: 
        print(e)
        
# if user selected the option for uploading csv file 
elif input_type == "Upload CSV File":
   file_upload()

else :
    pass


# api which i am using 
# https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol=IBM
