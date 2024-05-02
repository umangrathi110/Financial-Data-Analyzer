import os
import streamlit as st
from interpreter import interpreter
from langchain.chat_models import ChatOpenAI
from langchain_experimental.agents import create_csv_agent
from dotenv import load_dotenv
from langchain.agents.agent_types import AgentType
from ImageUpload import *


load_dotenv()

# Retrieve values from .env file
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def generate_graph(file, user_query, chart_type):
    
    client = create_csv_agent(
            ChatOpenAI(model='gpt-3.5-turbo', openai_api_key=OPENAI_API_KEY, temperature=0.5), 
            file, 
            agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            handle_parsing_errors=True,
            verbose=True
        )
    # spinner widget is a visual element in user interface design that indicates to the user that a process is ongoing or in progress.
    with st.spinner(f"Generating response for: {user_query}"):
        response = client.run(user_query)
        st.text_area("Response", value=response)

        # interpreter used for NLP tasks takes the input response and generate the code for chart creation
        interpreter.model= "gpt-3.5-turbo"
        if chart_type == "Default":
            graph_created = interpreter.chat('Select best suitable graph for data =' + response +' and name it as csv_graph.png and save it in current folder and return the path of created file in string format.')
        else:
            graph_created = interpreter.chat('Create a ' + chart_type + ' for data=' + response+' and name it as csv_graph.png and save it in current folder and return the path of created file in string format.')
        if graph_created :
            uploaded_image = uploadImageOnCloud("csv_graph.png")
            st.image(uploaded_image, caption='Uploaded to Cloudinary successfully', use_column_width=True)
    