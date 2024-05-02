import streamlit as st
import os 
import json
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.callbacks import get_openai_callback
from dotenv import load_dotenv
from prompt import *
from ImageUpload import *


#Load environment Variables
load_dotenv()

# Retrieve values from .env file
openai_api_key = os.getenv("OPENAI_API_KEY")


def get_answer(question, json, chart): 

    try:
        llm = ChatOpenAI(temperature=0.0,model_name='gpt-3.5-turbo', verbose=True) 
        chain = LLMChain(llm=llm, prompt=PROMPT)

    except Exception as e:
        print(e)
    
    with get_openai_callback() as cb:
      inputs = {
          'input_json': input_json,  # Add the input JSON data from prompt file
          'question': question, # Add your question
          'chart' : chart
      }
      result = chain(inputs)
    return result, cb

def generate_llm_answer(query_status, user_question, json_data, chart_type):
    if query_status:
        with st.spinner(f"Generating response for: {user_question}"):
            response, cb = get_answer(user_question, json_data, chart_type)
            #To calculate cost and token size
            print(cb)
            
            result = ""

            if "I don't know!" not in response and "I'm sorry" not in response:
                response = response['text']
                print(response)

                # executing the function which is in string format 
                exec_globals = {}
                exec(response, exec_globals)
                
                if 'output' in exec_globals:
                    output = exec_globals['output']
                    # print(output)
                    input_json = json.loads(json_data)
                    result = output(input_json)
                    print(result)  # Print the result returned by the function
                else:
                    print("Function output not found.")

                if "Function output not found." not in result:
                    #upload graph in cloud
                    upload_image = uploadImageOnCloud(result)
                    st.image(upload_image, caption='Uploaded to Cloudinary successfully', use_column_width=True)

                else :
                    st.error("Unable to generate the Graph")




